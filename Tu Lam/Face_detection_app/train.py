from loaddata.loaddataset import MasterImage
from Face_Detection.face_detection import FaceDetection
import cv2

EPOCHS = 300
INIT_LR = 1e-3
BS = 32
height, width = 300, 400


path = '/Users/taanhtuan/Desktop/PycharmProject/ML project/Tu lam/Face_detection_app/Dataset'
a = MasterImage(PATH=path, Height = height, Width = width)

trainX,trainY = a.load_dataset()
list_of_classes = a.get_categories()
num_of_classes = len(list_of_classes)



cascPath = "haarcascade_frontalface_default.xml"
path2 = "/Users/taanhtuan/Desktop/PycharmProject/ML project/Tu lam/Face_detection_app/Dataset/donald trump/1.jpeg"

faceCascade = cv2.CascadeClassifier(cascPath)


for i in range(len(trainX)):
    faceImage = FaceDetection.detect(trainX[i], faceCascade)
    cv2.imshow("Face Image", faceImage)
    cv2.waitKey(0)



