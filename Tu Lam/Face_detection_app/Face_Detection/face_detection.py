# import the necessary packages
import cv2


class FaceDetection:

	@staticmethod
	def detect(image,faceCascade):


		cv2.imshow("Image", image)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		faces = faceCascade.detectMultiScale(
			gray,
    		scaleFactor=1.1,
    		minNeighbors=5,
    		minSize=(30, 30),
    		flags=cv2.CASCADE_SCALE_IMAGE)
		print("Found {0} faces!".format(len(faces)))
		num_of_face = 0
		# Draw a rectangle around the faces
		for (x, y, w, h) in faces:
			cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

			num_of_face += 1
			image_name = 'face' + str(num_of_face)
			cropped = image[y:y + h, x:x + w]
			cv2.imwrite("/Users/taanhtuan/Desktop/PycharmProject/ML project/Tu lam/Face_detection_app/Face_Data/" + image_name + ".png",cropped)
			break

		cv2.imshow("Faces found", image)
		cv2.waitKey(0)

		return gray






