import tensorflow as tf
import cv2
import os
import pickle
import numpy as np



class MasterImage(object):

    def __init__(self,PATH='', Height = 50, Width = 50):
        self.PATH = PATH
        self.Height = Height
        self.Width = Width

        self._image_data = []
        self._x_data = []
        self._y_data = []
        self._categories = []


    def set_categories(self):
        for path in os.listdir(self.PATH):
            if '.DS_Store' not in path:
                self._categories.append(path)
        print("Found Categories ",self._categories,'\n')

    def get_categories(self):
        return self._categories

    def process_image(self):
        try:
            self.set_categories()
            for category in self._categories:                                                  # Iterate over categories

                train_folder_path = os.path.join(self.PATH, category)                         # Folder Path
                class_index = self._categories.index(category)                                 # this will get index for classification

                for img in os.listdir(train_folder_path):                                       # This will iterate in the Folder
                    new_path = os.path.join(train_folder_path, img)
                    # image Path

                    try:        # if any image is corrupted
                        image_data_temp = cv2.imread(new_path)
                        # Read Image as numbers
                        image_temp_resize = cv2.resize(image_data_temp,(self.Height,self.Width))
                        self._x_data.append(image_temp_resize)  # Get the X_Data
                        self._y_data.append(class_index)  # get the label
                    except:
                        pass


            X_Data = np.asarray(self._x_data)
            Y_Data = np.asarray(self._y_data)


            return X_Data, Y_Data
        except:
            print("Failed to run Function Process Image ")

    def pickle_image(self):

        """
        :return: None Creates a Pickle Object of DataSet
        """
        # Call the Function and Get the Data
        X_Data,Y_Data = self.process_image()

        # Write the Entire Data into a Pickle File
        pickle_out = open('X_Data','wb')
        pickle.dump(X_Data, pickle_out)
        pickle_out.close()

        # Write the Y Label Data
        pickle_out = open('Y_Data', 'wb')
        pickle.dump(Y_Data, pickle_out)
        pickle_out.close()

        print("Pickled Image Successfully ")
        return X_Data,Y_Data

    def load_dataset(self):

        try:
            # Read the Data from Pickle Object

            X_Temp = open('X_Data','rb')
            X_Data = pickle.load(X_Temp)

            Y_Temp = open('Y_Data','rb')
            Y_Data = pickle.load(Y_Temp)

            self.CATEGORIES = self.set_categories()

            print('Reading Dataset from PIckle Object')

            return X_Data,Y_Data

        except:
            print('Could not Found Pickle File ')
            print('Loading File and Dataset  ..........')

            X_Data,Y_Data = self.pickle_image()
            return X_Data,Y_Data





















