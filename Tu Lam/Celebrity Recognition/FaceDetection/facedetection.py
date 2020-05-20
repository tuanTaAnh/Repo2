from FaceDetection.encode_faces import FaceEncoding
from FaceDetection.cluster_faces import FaceClustering
import os

class FaceDect:

    @staticmethod
    def faceclutering(catapath, savepath, encodepath):


        if os.path.isfile(encodepath):
            print("FOUND")
        else:
            FaceEncoding.encode(catapath,encodepath)

        try:
            os.mkdir(savepath)
            print("Directory ", savepath, " Created ")
        except FileExistsError:
            print("Directory ", savepath, " already exists")

        FaceClustering.clustering(savepath,encodepath)