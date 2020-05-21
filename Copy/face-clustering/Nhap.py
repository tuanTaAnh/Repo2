import cv2
import os

path = "/Users/taanhtuan/Desktop/PycharmProject/face-clustering/dataset/00000000.jpg"
image = cv2.imread(path)

# Create directory
newpath = '/Users/taanhtuan/Desktop/PycharmProject/face-clustering/Data/data1'
try:
    # Create target Directory
    os.mkdir(newpath)
    print("Directory " , newpath ,  " Created ")
except FileExistsError:
    print("Directory " , newpath ,  " already exists")

cv2.imwrite(newpath + '/' + 'image.jpg',image)