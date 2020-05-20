import os
from FaceDetection.facedetection import FaceDect
from FaceDetection.encode_faces import FaceEncoding
from FaceDetection.cluster_faces import FaceClustering


class LoadData:

    @staticmethod
    def Load(PATH):
        categories = []
        for path in os.listdir(PATH):
            if '.DS_Store' not in path:
                categories.append(path)
        print("Found Categories " ,len(categories) ,'\n')
        for (i,category) in enumerate(categories):
            catapath = PATH + '/' + category
            savepath = "/Users/taanhtuan/Desktop/PycharmProject/Celebrity Recognition/FaceData/Face" + str(i)
            encodepath = "/Users/taanhtuan/Desktop/PycharmProject/Celebrity Recognition/EncodeData/encodings" + str(i) + ".pickle"
            FaceDect.faceclutering(catapath,savepath,encodepath)
        # catapath = PATH + '/' + categories[0]
        # savepath = "/Users/taanhtuan/Desktop/PycharmProject/Celebrity Recognition/FaceData/Face" + str(0)
        # encodepath = "/Users/taanhtuan/Desktop/PycharmProject/Celebrity Recognition/EncodeData/encodings" + str(0) + ".pickle"
        # FaceDect.faceclutering(catapath, savepath, encodepath)
