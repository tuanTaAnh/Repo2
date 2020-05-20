import cv2
from DataLoad.pretrain_data import LoadData
from FaceDetection.cluster_faces import FaceClustering

path = "/Users/taanhtuan/Desktop/PycharmProject/data/celebrity dataset"

LoadData.Load(path)