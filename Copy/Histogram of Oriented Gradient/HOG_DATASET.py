from loaddata.loaddataset import MasterImage
from HOG1.implement import Feature_Extraction
import cv2
import numpy as np
from numpy import linalg as LA
from sklearn.model_selection import KFold, train_test_split


class HOG:
    @staticmethod
    def get_data_output(data_input):
        data_output = []
        for i in range(len(data_input)):
            vector = Feature_Extraction.hog(data_input[i])
            print('Feature size:', vector.shape)
            print('Features (HOG):', vector)
            data_output.append(vector)
        return data_output


height, width = 150, 150
path = '/Users/taanhtuan/Desktop/PycharmProject/ML project/Tu lam/Celebrities regconition/Dataset'
a = MasterImage(PATH=path, Height = height, Width = width)
data,labels = a.load_dataset()

print(data.shape)
print(labels.shape)
print()
cv2.imshow("DATA",data[0])
cv2.waitKey(0)
cv2.destroyAllWindows()

#(trainX, testX, trainY, testY) = train_test_split(data, labels, test_size=0.15, random_state=42)

print("==============================")
img1 = cv2.imread("/Users/taanhtuan/Desktop/PycharmProject/ML project/Tu lam/Celebrities regconition/Dataset/mohamed salah/1.jpeg"
                  , cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(src=img1, dsize=(height, width))
img1 = np.asarray(img1)
print("img1")
cv2.imshow("image",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

f = Feature_Extraction.hog(img1)
print('Feature size:', f.shape)
print('Features (HOG):', f)

print("==============================")

data = np.asarray(HOG.get_data_output(data))

print(data.shape)



















