import cv2
import os

PATH = "/Users/taanhtuan/Desktop/PycharmProject/Face_Detection/Dataset/donald trump"
face_cascade = cv2.CascadeClassifier("face.xml") # DEFAULT _ FACE
trump_face = []

for img_name in os.listdir(PATH):
    if '.DS_Store' not in img_name:
        image = cv2.imread(PATH + '/' + img_name)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            face_resized_img = cv2.resize(image[y:y + h, x:x + w], (300, 300), interpolation=cv2.INTER_AREA)
            trump_face.append(face_resized_img)
            cv2.imwrite("/Users/taanhtuan/Desktop/PycharmProject/Face_Detection/FaceData/" + img_name + '.jpg', face_resized_img)

for image in trump_face:
    cv2.imshow()


