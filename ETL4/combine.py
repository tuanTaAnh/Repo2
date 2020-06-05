import glob
import random
import os
import glob
import random
import os
from PIL import Image
import cv2
import numpy as np
from scipy import ndimage
import imutils
import math


data_path = r"/Users/taanhtuan/Desktop/combine_images/Data/ETL4/*"
denoised_path = r"/Users/taanhtuan/Desktop/combine_images/Data/denoised_ETL4/*"
compared_path = r"/Users/taanhtuan/Desktop/combine_images/Data/compared_ETL4/"
hor_image_path = r"/Users/taanhtuan/Desktop/combine_images/Data/horizontal_combined_images/"
ver_image_path = r"/Users/taanhtuan/Desktop/combine_images/Data/vertical_combined_images/"
num_of_images = 3


def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):

    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    print("Len: ",len(im_list_resize))
    return cv2.vconcat(im_list_resize)


def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv2.hconcat(im_list_resize)


def detele_files(path):
    for f in glob.glob(path + "*"):
        os.remove(f)


def combine_image(image_path_set,num_of_images,ver_image_path,hor_image_path):

    img_list = []
    random_image_set = random.sample(image_path_set, k=num_of_images)

    print("Len: ", len(random_image_set))
    str_name = ""
    for imagepath in random_image_set:
        # print(imagepath)
        img = cv2.imread(imagepath)
        img_list.append(img)

        img_name = (imagepath.split("result")[-1]).split(".")[0]
        str_name += "_" + img_name

    print("str_name: ",str_name)

    print("Len: ", len(img_list))
    print(len(random_image_set))

    im_v_resize = vconcat_resize_min(img_list)
    cv2.imwrite(ver_image_path + "ver" + str_name + ".png", im_v_resize)


    im_h_resize = hconcat_resize_min(img_list)
    cv2.imwrite(hor_image_path + "hor" + str_name + ".png", im_h_resize)


def combine_word():
    image_path_set = []

    for imagepath in glob.glob(data_path):
        image_path_set.append(imagepath)

    detele_files(ver_image_path)
    detele_files(hor_image_path)


    for i in range(10):
        print(i," : ")
        combine_image(image_path_set, num_of_images, ver_image_path, hor_image_path)


def combine_origin_and_denoised():

    for img1_path in glob.glob(data_path):

        img_name = img1_path.split("/")[-1]
        print(img_name)
        img2_path = denoised_path[:-len(os.path.basename(denoised_path))] + "result" + img_name
        # print(img2_path)

        img1 = cv2.imread(img1_path)
        img2 = cv2.imread(img2_path)

        # print(img1.shape)
        # print(img2.shape)

        img_list = [img1,img2]

        im_h_resize = hconcat_resize_min(img_list)
        cv2.imwrite(compared_path + "compared" + img_name, im_h_resize)



if __name__ == "__main__":
    # combine_word()
    combine_origin_and_denoised()















