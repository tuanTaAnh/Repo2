import os, sys
import cv2


def apply_roi(img, roi):
    # resize ROI to match the original image size
    roi = cv2.resize(src=roi, dsize=(img.shape[1], img.shape[0]))

    assert img.shape[:2] == roi.shape[:2]

    # scale ROI to [0, 1] => binary mask
    thresh, roi = cv2.threshold(roi, thresh=128, maxval=1, type=cv2.THRESH_BINARY)

    # apply ROI on the original image
    new_img = img * roi
    return new_img


if __name__ == "__main__":


    path1 = "/Users/taanhtuan/Desktop/PycharmProject/Machine Learning cơ bản/Computer Vision/Region of Interest/img_4.jpg"
    path2 = "/Users/taanhtuan/Desktop/PycharmProject/Machine Learning cơ bản/Computer Vision/Region of Interest/ROI.png"
    path3 = "/Users/taanhtuan/Desktop/PycharmProject/Machine Learning cơ bản/Computer Vision/Region of Interest/img_4_new.jpg"

    img = cv2.imread(path1)  # shape: (588, 586, 3)
    roi = cv2.imread(path2)  # shape: (300, 300, 3)

    new_img = apply_roi(img, roi)

    cv2.imwrite(path3, new_img)