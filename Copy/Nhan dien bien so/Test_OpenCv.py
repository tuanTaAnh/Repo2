import numpy as np
import cv2
import  imutils


image = cv2.imread('car.jpeg')

image = imutils.resize(image, width=500)

cv2.imshow("Original Image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("1 - Grayscale Conversion", gray)
cv2.imwrite("image_gray.jpeg", gray)

gray = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow("2 - Bilateral Filter", gray)
cv2.imwrite("image_bilateral.jpeg", gray)
edged = cv2.Canny(gray, 170, 200)
cv2.imshow("4 - Canny Edges", edged)
cv2.imwrite("image_cany.jpeg", edged)

(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30]

NumberPlateCnt = []
tmp = image.copy()

count = 0
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    cv2.drawContours(tmp, [c], -1, (0,0,128), 2)
    #cv2.drawContours(tmp, [approx], -1, (0,255,0), 2)
    if len(approx) == 4:
        NumberPlateCnt.append(approx)

cv2.imwrite("image_countour.jpeg", tmp)

for plate in NumberPlateCnt:
    cv2.drawContours(image, [plate], -1, (0,255,0), 2)

cv2.imshow("Final Image With Number Plate Detected", image)
cv2.imwrite("image_result.jpeg", image)

cv2.waitKey(0)