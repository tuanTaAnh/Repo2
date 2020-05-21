import tensorflow as tf
import cv2
import os
import pickle
import numpy as np


class MasterImage(object):

    def __init__(self,PATH='', Height = 80, Width = 80):
        self.PATH = PATH
        self.Height = Height
        self.Width = Width

        self.image_data = []
        self.x_data = []
        self.y_data = []
        self.CATEGORIES = []

        # This will get List of categories
        self.list_categories = []

    def get_categories(self):
        for path in os.listdir(self.PATH):
            if '.DS_Store' in path:
                pass
            else:
                self.list_categories.append(path)
        print("Found Categories ",self.list_categories,'\n')
        return self.list_categories

    def Process_Image(self):
        try:
            """
            Return Numpy array of image
            :return: X_Data, Y_Data
            """
            self.CATEGORIES = self.get_categories()
            for categories in self.CATEGORIES:                                                  # Iterate over categories

                train_folder_path = os.path.join(self.PATH, categories)                         # Folder Path
                class_index = self.CATEGORIES.index(categories)                                 # this will get index for classification

                for img in os.listdir(train_folder_path):                                       # This will iterate in the Folder
                    new_path = os.path.join(train_folder_path, img)                             # image Path

                    try:        # if any image is corrupted

                        image_data_temp = cv2.imread(new_path,cv2.IMREAD_GRAYSCALE)                 # Read Image as numbers
                        image_temp_resize = cv2.resize(image_data_temp, (self.Height, self.Width))
                        self.x_data.append(image_temp_resize)  # Get the X_Data
                        self.y_data.append(class_index)  # get the label

                    except:
                        pass


            X_Data = np.asarray(self.x_data)
            Y_Data = np.asarray(self.y_data)

            return X_Data, Y_Data
        except:
            print("Failed to run Function Process Image ")


    def load_dataset(self):

        X_Data, Y_Data = self.Process_Image()

        return X_Data,Y_Data
