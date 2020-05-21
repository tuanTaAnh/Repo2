import cv2
import glob

# create a function to grab each image, detect the face, crop the face, save the face image
def crop_faces(path, scale):
    # grabs all image directory paths
    img_list = glob.glob(path + '/*.jpg')

    # face cascade from OpenCV
    cascPath = "/Users/taanhtuan/Desktop/PycharmProject/Face_Detection/haarcascade_frontalface_default.xml"
    haar_face_cascade = cv2.CascadeClassifier(cascPath)
    k = 0
    for img_name in img_list:
        k += 1
        print(k," : ",img_name)
        img = cv2.imread(img_name)
        cv2.imshow("Image", img)
        cv2.waitKey(0)


        faces = haar_face_cascade.detectMultiScale(img, scaleFactor=scale, minNeighbors=5)

        # resize cropped images
        for (x, y, w, h) in faces:
            face_cropped = img[y:y + h, x:x + w]
            face_resized_img = cv2.resize(img[y:y + h, x:x + w], (175, 175), interpolation=cv2.INTER_AREA)
            # save cropped face images
            new_img_name = img_name.replace('.jpg', '')
            print("1.")
            cv2.imwrite( new_img_name + '.jpg', face_resized_img)
            print("2.")
            #cv2.imshow("Image", face_cropped)
            #cv2.waitKey(0)
            cv2.imshow("Image",face_resized_img)
            cv2.waitKey(0)



path = "/Users/taanhtuan/Desktop/PycharmProject/Face_Detection/Dataset/donald trump"
scale = 2
crop_faces(path,scale)