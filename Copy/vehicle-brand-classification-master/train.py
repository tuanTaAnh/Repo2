# USAGE
# python train.py --dataset dataset --model brandNet.model --labelbin lb.pickles

# set the matplotlib backend so figures can be saved in the background
import matplotlib
matplotlib.use("Agg")

# import the necessary packages
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.preprocessing.image import img_to_array
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from cnnmodel.smallervggnet import SmallerVGGNet
from loaddata.loaddataset import MasterImage
import matplotlib.pyplot as plt
from imutils import paths
import numpy as np
import argparse
import random
import pickle
import cv2
import os


# initialize the number of epochs to train for, initial learning rate,
# batch size, and image dimensions
EPOCHS = 300
INIT_LR = 1e-3
BS = 32
IMAGE_DIMS = (90, 120, 3)

path = '/Users/taanhtuan/Desktop/PycharmProject/ML project/Test Demo/dataset'

a = MasterImage(PATH=path, IMAGE_DIMS = (120, 90, 3))

data,labels = a.load_dataset()
list_of_classes = a.get_categories()
print(list_of_classes)
print(data.shape)
print(labels.shape)

list_of_class = a.get_categories()


#scale the raw pixel intensities to the range [0, 1]
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)
print("[INFO] data matrix: {:.2f}MB".format(
	data.nbytes / (1024 * 1000.0)))

# binarize the labels
lb = LabelBinarizer()
labels = lb.fit_transform(labels)


# partition the data into training and testing splits using 80% of
# the data for training and the remaining 20% for testing
(trainX, testX, trainY, testY) = train_test_split(data, labels, test_size=0.15, random_state=42)


# initialize the model
print("[INFO] compiling model...")
model = SmallerVGGNet.build(
		width=IMAGE_DIMS[1],
		height=IMAGE_DIMS[0],
		depth=IMAGE_DIMS[2],
		classes=len(list_of_classes)
	)

opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
model.compile(
		optimizer=opt,
		loss="categorical_crossentropy",
		metrics=["accuracy"]
	)

# construct the image generator for data augmentation
aug = ImageDataGenerator(
	rotation_range=25,
	width_shift_range=0.1,
	height_shift_range=0.1,
	shear_range=0.2,
	zoom_range=0.2,
	horizontal_flip=True,
	fill_mode="nearest")

# train the network
print("[INFO] training network...")
H = model.fit_generator(
		aug.flow(trainX, trainY, batch_size=BS),
		validation_data=(testX, testY),
		steps_per_epoch=len(data) // BS,
		epochs=EPOCHS,
		verbose=1
	)


