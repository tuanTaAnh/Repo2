import cv2
import os
import glob

class ReadDataSet:

    @staticmethod
    def crop_faces(path, scale):
        # grabs all image directory paths
        img_list = glob.glob(path + '/*.jpg')

        # face cascade from OpenCV
        trump_face = []
        num_of_faceimage = 0
        num_of_image = 0
        haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

        for img_name in img_list:
            try:
                num_of_image += 1
                img = cv2.imread(img_name)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = haar_face_cascade.detectMultiScale(gray, scaleFactor=scale, minNeighbors=5)

                # resize cropped images
                for (x, y, w, h) in faces:
                    num_of_faceimage += 1
                    face_resized_img = cv2.resize(gray[y:y + h, x:x + w], (175, 175), interpolation=cv2.INTER_AREA)

                    # save cropped face images
                    new_img_name = img_name.replace('.jpg', '')
                    trump_face.append(face_resized_img)
                    cv2.imwrite("/Users/taanhtuan/Desktop/PycharmProject/Face_Detection_2/Face_Data/" + str(
                        num_of_faceimage) + '.jpg', face_resized_img)
                    print(num_of_image, ": ", new_img_name)
            except:
                print(num_of_image, ": ", new_img_name)


        return trump_face