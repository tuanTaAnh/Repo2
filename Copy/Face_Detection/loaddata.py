import cv2
import os
from imutils.object_detection import non_max_suppression
import imutils
import numpy as np

PATH = "/Users/taanhtuan/Desktop/PycharmProject/Face_Detection/Dataset"
categories = []
x_data = []
y_data = []

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

for path in os.listdir(PATH):
    if '.DS_Store' not in path:
        categories.append(path)
print("Found Categories ", categories, '\n')

for category in categories:  # Iterate over categories
    train_folder_path = os.path.join(PATH, category)  # Folder Path
    class_index = categories.index(category)

    for img in os.listdir(train_folder_path):  # This will iterate in the Folder
        new_path = os.path.join(train_folder_path, img)
        try:  # if any image is corrupted
            image_data_temp = cv2.imread(new_path)
            # Read Image as numbers
            x_data.append(image_data_temp)  # Get the X_Data
            y_data.append(class_index)  # get the label
        except:
            pass

X_Data = np.asarray(x_data)
Y_Data = np.asarray(y_data)

for img in X_Data:
    cv2.imshow("Image",img)
    cv2.waitKey(0)