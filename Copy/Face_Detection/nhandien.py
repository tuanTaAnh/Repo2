

# NGUYEN LY HOAT DONG CUA CHUONG TRINH
# DAU TIEN CHUONG TRINH SE:
# LOAD THU VIEN CAN THIET

import numpy as np # THU VIEN SU DUNG MANG (ARRAY)
import cv2 # THU VIEN OPEN CV2 - SU DUNG DE NHAN DIEN KHUON MAT

# SAU KHI LOAD THU VIEN XONG
#TIEN HANH SU DUNG
#THU VIEN KHUONG MAT (MAC DINH TRONG OPENCV)
face_cascade = cv2.CascadeClassifier("face.xml") # DEFAULT _ FACE
haar_face_cascade = cv2.CascadeClassifier("/Users/taanhtuan/Desktop/PycharmProject/Face_Detection/haarcascade_frontalface_default.xml")

#MINH DUNG WEBCAME CUA MAY TINH NEN DUNG LENH NAY
#MOI NGUOI CO THE DUNG CAMERA IP - HOAC CAMERA KHAC TUY Y NHE
cap = cv2.VideoCapture(0)

# BIEN Y CHO BANG 0 THAM SO TRUYEN VAO BIEN
Y=0

# CHUONG TRINH SE LAP VONG VO HAN NHE WHILE (TRUE) SE KET THUC KHI HAM (if cv2.waitKey(1) & 0xFF == ord('q'):) NHES
while (True):
    # LOAD HINH ANH TU CAMERA WEBCAME
    ret, frame = cap.read()
    # CHUYEN ANH VE DANG ANH XAM (GRAY) DE XU LY NHAN DIEN NHANH NHE
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # SAU KHI ANH TU CAMERA WEBCAM DUOC THU VE. NO SE DUOC SU DUNG KET HOP VOI THU VIEN (FACE.XML) CHO GIA TRI KHUON MAT
    faces = face_cascade.detectMultiScale(gray)
    #faces = haar_face_cascade.detectMultiScale(frame, scaleFactor=2, minNeighbors=5)

    #LENH DE VE HINH VUONG BAO QUANH KHUON MAT NHAN DIEN DUOC
    for (x, y, w, h) in faces:
        # VE HINH VUONG THEO TRUC TOA DO (X, Y , W ,H) (TRUONG UNG)
        #GIA TRI HIEN THI
        #FRAME: HINH ANH LAY TU CAMERA WEBCAM
        #(X,Y) TOA DO DIEM DAU TIEN DE VE HINH VUONG
        #(X+W,Y+H) : LA TOA DO TINH TIEN
        #X: THEO CHIEU NGANG W
        #Y: THEO CHIEU CAO H
        # GIA TRI: (0, 255, 0) LA MAU HIEN TI (B-G-R)
        #GIA TRI ((0, 255, 0)) HIEN THI MAU XANH CUA HINH VUONG BAO QUANH KHUON MAT
        # MUON CHUYEN THANH MAU KHAC THI DOI LAI : VD MAU DO
        # THAM SO CUOI CUNG: 2 DO DAY CUA HINH VUONG
        # SO CANG > THI CANG DAY
        #VD: CHUYEN THAH 5
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)        
        #roi_color = frame[y:y + h, x:x + w]
        #
        # LIENH HIEN THI HINH ANH
        #TRONG DAU 'LA TEN CUA HINH ANH HIEN LEN'
    cv2.imshow('DETECTING FACE', frame)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
