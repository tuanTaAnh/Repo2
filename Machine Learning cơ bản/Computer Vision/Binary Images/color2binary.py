import os, sys
import cv2


def convert_to_binary(img_grayscale, thresh=100):
    thresh, img_binary = cv2.threshold(img_grayscale, thresh, maxval=255, type=cv2.THRESH_BINARY)
    return img_binary


if __name__ == "__main__":
    input_image_path = "img_5.jpg"

    # read color image with grayscale flag: "cv2.IMREAD_GRAYSCALE"
    img_grayscale = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)  # shape: (960, 960)
    cv2.imshow("Image",img_grayscale)
    # print grayscale image
    cv2.imwrite('grey_' + input_image_path, img_grayscale)

    print('Saved grayscale image @ grey_%s' % input_image_path)

    img_binary = convert_to_binary(img_grayscale, thresh=100)
    cv2.imwrite('binary_' + input_image_path, img_binary)

    print('Saved binary image @ binary_%s' % input_image_path)