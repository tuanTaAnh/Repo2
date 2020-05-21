# We are using a pre-trained model to map face images into 128-dimensional encodings
# FaceNet learns a neural network that encodes a face image into a vector of 128 numbers.
# By comparing two such vectors, you can then determine if two pictures are of the
# same person.

from core.utils import *
from core.inception_blocks import *
from database_client.database import Operations

from keras import backend as K
K.set_image_data_format('channels_first')
import cv2
import numpy as np
import tensorflow as tf
import logging
from configparser import ConfigParser, ExtendedInterpolation
import os


config_parser = ConfigParser(interpolation=ExtendedInterpolation())
config_parser.read('config.ini')
logger = logging.getLogger('fr.utils')
FACE_CASCADE_PATH = os.path.abspath(config_parser['OPEN_CV']['cascade_classifier_path'])
FACE_CASCADE = cv2.CascadeClassifier(FACE_CASCADE_PATH)


class CelebModelOperations(object):

    @staticmethod
    def _triplet_loss(y_true, y_pred, alpha = 0.2):
        """
        Implementation of the triplet loss.
        
        Arguments:
        y_true -- true labels, required when you define a loss in Keras,
                  we don't need it in this function.
        y_pred -- python list containing three objects:
                anchor -- the encodings for the anchor images, of shape (None, 128)
                positive -- the encodings for the positive images, of shape (None, 128)
                negative -- the encodings for the negative images, of shape (None, 128)
        
        Returns:
        loss -- real number, value of the loss
        """
        
        anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]
        
        # Compute the (encoding) distance between the anchor and the positive
        pos_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, positive)))
        # Compute the (encoding) distance between the anchor and the negative
        neg_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, negative)))
        # subtract the two previous distances and add alpha.
        basic_loss = tf.subtract(pos_dist, neg_dist) + alpha
        # Take the maximum of basic_loss and 0.0. Sum over the training examples.
        loss = tf.reduce_sum(tf.maximum(basic_loss, 0.0))
        
        return loss

    @staticmethod
    def who_is_it(facial_image_path, database, model):
        """
        Implements face recognition by finding who is the person on the image_path image.
        
        Arguments:
        image_path -- path to an image
        database -- database containing image encodings along with the name of the person on the image
        model -- Inception model instance in Keras
        
        Returns:
        min_dist -- the minimum distance between image_path encoding and the encodings from the database
        identity -- string, the name prediction for the person on image_path
        """
        
        # Compute the target "encoding" for the image.

        encoding = img_to_encoding(facial_image_path, model)
        
        # Find the closest encoding
        # Initialize "min_dist" to a large value, say 100
        min_dist = 100
        identity = None
        
        # Loop over the database dictionary's names and encodings.
        for celeb in database:
            
            # Compute L2 distance between the target "encoding" and the current "emb" from the database.
            dist = np.linalg.norm(encoding - celeb.encodings)

            # If this distance is less than the min_dist, then set min_dist to dist, and identity to name.
            if dist < min_dist:
                min_dist = dist
                identity = celeb.name
        
        if min_dist > 0.85:
            print("Not in the database.")
        else:
            print ("it's " + str(identity) + ", the distance is " + str(min_dist))
            
        return min_dist, identity

    @staticmethod
    def face_extractor(img_path):
        tx, ty, tw, th = (None, None, None, None)

        img = cv2.imread(img_path, -1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = FACE_CASCADE.detectMultiScale(gray, 1.3, 5)
        
        if faces == ():
            return None

        for (x,y,w,h) in faces:
            face = cv2.resize(img[y:y+h, x:x+w, :], (96, 96))
            loc = 'static/images/temp.jpg'
            cv2.imwrite(loc, face)
            tx, ty, tw, th = (x, y, w, h)

        cv2.rectangle(img, (tx,ty), (tx+tw, ty+th), (0, 255, 0), 3)
        cv2.imwrite(img_path, img)
        return loc

    @staticmethod
    def add_new_celeb(image_path, celeb_name, model):
        facial_image_path = CelebModelOperations.face_extractor(image_path)
        
        if facial_image_path is None:
            logger.error('face not found in image: {image_path}'.format(
                image_path=image_path
            ))
            return False

        encodings = img_to_encoding(facial_image_path, model)
        celeb_id = Operations.add_celeb(celeb_name, encodings)
        return celeb_id

    @staticmethod
    def recognize_celebs(image_path, model):
        celeb_database = Operations.get_celebs()
        if celeb_database.count() == 0:
            logger.debug('Database empty')
            return None
        else:
            facial_image_path = CelebModelOperations.face_extractor(image_path)

            if facial_image_path is None:
                logger.error('face not found in image: {image_path}'.format(
                    image_path=image_path
                ))
                return

            dist, face_identity = CelebModelOperations.who_is_it(
                facial_image_path, celeb_database, model
            )
            return face_identity


class CelebModel(object):
    def __init__(self):
        self.fr_model = faceRecoModel(input_shape=(3, 96, 96))
        logger.info('celeb_model creation done.')
        self.fr_model.compile(
            optimizer='adam', loss=CelebModelOperations._triplet_loss, metrics=['accuracy']
        )
        logger.info('celeb_model compilation done.')
        load_weights_from_FaceNet(self.fr_model)
        logger.info('celeb_model weight loading done.')
