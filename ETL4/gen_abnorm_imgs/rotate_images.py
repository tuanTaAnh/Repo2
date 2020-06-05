import cv2
import numpy as np
import math

def padding_image(img):
    ht, wd, cc = img.shape

    # create new image of desired size and color (blue) for padding
    ww = 300
    hh = 300
    color = (255, 255, 255)
    result = np.full((hh, ww, cc), color, dtype=np.uint8)

    # compute center offset
    xx = (ww - wd) // 2
    yy = (hh - ht) // 2

    # copy img image into center of result image
    result[yy:yy + ht, xx:xx + wd] = img

    return result


def rotate_padding_image(image, angle):#parameter angle in degrees

    if len(image.shape) > 2:#check colorspace
        shape = image.shape[:2]
    else:
        shape = image.shape
    image_center = tuple(np.array(shape)/2)#rotation center

    radians = math.radians(angle)

    x, y,_ = image.shape
    new_x = math.ceil(math.cos(radians)*x + math.sin(radians)*y)
    new_y = math.ceil(math.sin(radians)*x + math.cos(radians)*y)
    new_x = int(new_x)
    new_y = int(new_y)
    rot_mat = cv2.getRotationMatrix2D(image_center,angle,1.0)

    result = cv2.warpAffine(image, rot_mat, shape, flags=cv2.INTER_LINEAR)

    return result

def crop_image(rotated_img, w, dw, h, dh):
    result = rotated_img[w:w+dw, h:h+dh]
    return result


def rotate_image(img):

    pad_img = padding_image(img)

    rotated_img = rotate_padding_image(pad_img, -30)

    cropped_img = crop_image(rotated_img, 120, 62, 120, 64)

    return cropped_img


if __name__ == "__main__":
    # read image
    img = cv2.imread(r'/Users/taanhtuan/Desktop/combine_images/Data/Image.png')

    result = rotate_image(img)

    # view result
    cv2.imshow("result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # save result
    cv2.imwrite(r"/Users/taanhtuan/Desktop/combine_images/Data/rotated_image.png", result)