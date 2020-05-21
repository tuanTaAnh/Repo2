import cv2
import os
import numpy as np
from sklearn.cluster import KMeans
from HOG.hog import HOG
from loaddata.loaddata import ReadDataSet

PATH = "/Users/taanhtuan/Desktop/PycharmProject/Face_Detection_2/Dataset/Aaron Judge"


trump_face = ReadDataSet.crop_faces(PATH,2)

trump_face = np.asarray(trump_face)
print(trump_face.shape)




