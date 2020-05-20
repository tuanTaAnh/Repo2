import cv2
import numpy as np
from numpy import linalg as LA
from imutils import paths
import pickle
import face_recognition


class FaceEncoding:

    @staticmethod
    def encode(catapath,encodepath):

        DETECTION_METHOD_PATH = -1

        # grab the paths to the input images in our dataset, then initialize
        # out data list (which we'll soon populate)
        print("[INFO] quantifying faces...")
        imagePaths = list(paths.list_images(catapath))
        data = []
        num_of_image = 0
        num_of_faceimage = 0

        # loop over the image paths
        for (i, imagePath) in enumerate(imagePaths):
            try:
                # load the input image and convert it from RGB (OpenCV ordering)
                # to dlib ordering (RGB)
                print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))
                print(imagePath)
                image = cv2.imread(imagePath)
                rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                # detect the (x, y)-coordinates of the bounding boxes
                # corresponding to each face in the input image
                boxes = face_recognition.face_locations(rgb, model=DETECTION_METHOD_PATH)

                # compute the facial embedding for the face
                encodings = face_recognition.face_encodings(rgb, boxes)

                d = [ {"imagePath": imagePath, "loc": box, "encoding": enc}
                     for (box, enc) in zip(boxes, encodings) ]
                data.extend(d)
                for box in boxes:
                    (top, right, bottom, left) = box
                    face = image[top:bottom, left:right]
                    # num_of_faceimage += 1
                    # cv2.imwrite("/Users/taanhtuan/Desktop/PycharmProject/face-clustering/Face_data/" + str(num_of_faceimage) + ".jpg", face)
                num_of_image += 1
            except:
                pass

        # dump the facial encodings data to disk
        print("[INFO] serializing encodings...")
        f = open(encodepath, "wb")
        f.write(pickle.dumps(data))
        f.close()