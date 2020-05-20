# USAGE
# python cluster_faces.py --encodings encodings.pickle

# import the necessary packages
from sklearn.cluster import DBSCAN
from imutils import build_montages
import numpy as np
import argparse
import os
import pickle
import cv2

class FaceClustering:

	def save(self):
		print()


	@staticmethod
	def clustering(savepath,encodepath):

		JOBS = -1
		num = 0
		num_of_face = 0

		print("[INFO] loading encodings...")
		data = pickle.loads(open(encodepath, "rb").read())
		data = np.array(data)
		encodings = [d["encoding"] for d in data]

		# cluster the embeddings
		print("[INFO] clustering...")
		clt = DBSCAN(metric="euclidean", n_jobs=JOBS)
		clt.fit(encodings)

		# determine the total number of unique faces found in the dataset
		labelIDs = np.unique(clt.labels_)
		print(len(encodings))
		print(encodings[667].shape)
		print(labelIDs)
		numUniqueFaces = len(np.where(labelIDs > -1)[0])
		print("[INFO] # unique faces: {}".format(numUniqueFaces))

		maxlabelID = -100
		maxValue = -100


		for labelID in labelIDs:

			idxs = np.where(clt.labels_ == labelID)[0]
			if len(idxs) > maxValue:
				maxlabelID = labelID
				maxValue = len(idxs)
			print("[INFO] faces for face ID: {}, {}".format(labelID,len(idxs)))



		num_of_image = 0
		max_idxs = np.where(clt.labels_ == maxlabelID)[0]

		try:
			os.mkdir(savepath)
			print("Directory ", savepath, " Created ")
		except FileExistsError:
			print("Directory ", savepath, " already exists")

		print(maxlabelID)
		print(len(max_idxs))

		for i in max_idxs:
			image = cv2.imread(data[i]["imagePath"])
			(top, right, bottom, left) = data[i]["loc"]
			face = image[top:bottom, left:right]
			num_of_image += 1

			face = cv2.resize(face, (175, 175))
			cv2.imwrite(savepath + '/' + str(num_of_image) + '.jpg', face)