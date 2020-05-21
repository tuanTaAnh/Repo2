import cv2
import sys

# Get user supplied values
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
face_cascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread("/Users/taanhtuan/Desktop/PycharmProject/ML project/Tu lam/Face_detection_app/Dataset/donald trump/25.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# SAU KHI ANH TU CAMERA WEBCAM DUOC THU VE. NO SE DUOC SU DUNG KET HOP VOI THU VIEN (FACE.XML) CHO GIA TRI KHUON MAT
faces = face_cascade.detectMultiScale(gray)

#LENH DE VE HINH VUONG BAO QUANH KHUON MAT NHAN DIEN DUOC
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #roi_color = frame[y:y + h, x:x + w]
    #
    # LIENH HIEN THI HINH ANH
    #TRONG DAU 'LA TEN CUA HINH ANH HIEN LEN'
cv2.imshow('DETECTING FACE', image)
cv2.waitKey(0)
