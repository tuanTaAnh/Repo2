import cv2

path = "/ML project/Tu lam/Celebrities regconition/Dataset/leonardo dicaprio/6.jpeg"
img = cv2.imread(path)

cv2.imshow("Image",img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image",gray)
cv2.waitKey(0)

