import cv2
import numpy as np
import glob

path = r"/Users/taanhtuan/Desktop/combine_images/Data/ETL4/56.png"
data_path = r"/Users/taanhtuan/Desktop/combine_images/Data/ETL4/*"
denoised_image_path = r"/Users/taanhtuan/Desktop/combine_images/Data/denoised_ETL4/result"

def resize_image(img):
    scale_percent = 200  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    return resized


def padding_image(img):
    ht, wd, cc = img.shape

    # create new image of desired size and color (blue) for padding
    ww = 75
    hh = 75
    color = (0, 100, 0)
    result = np.full((hh, ww, cc), color, dtype=np.uint8)

    # compute center offset
    xx = (ww - wd) // 2
    yy = (hh - ht) // 2

    # copy img image into center of result image
    result[yy:yy + ht, xx:xx + wd] = img

    return result


def crop_image(rotated_img, w, dw, h, dh):
    result = rotated_img[w:w+dw, h:h+dh]
    return result


if __name__ == "__main__":
    image_path_set = []

    for imagepath in glob.glob(data_path):
        image_path_set.append(imagepath)


    for image_path in image_path_set:
        img = cv2.imread(image_path)
        # img = crop_image(img,15,50,20,30)
        # img = padding_image(img)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img_name = image_path.split("/")[-1]

        h, w = gray_img.shape
        result = gray_img.copy()
        for i in range(h):
            for j in range(w):
                if gray_img[i][j] > 90:
                    result[i][j] = min(gray_img[i][j] + 20, 255)
                else:
                    result[i][j] = 48
        print("result" + img_name)

        cv2.imwrite(denoised_image_path + img_name, result)













