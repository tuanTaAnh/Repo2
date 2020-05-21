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

ENCODINGS_PATH = '/Users/taanhtuan/Desktop/PycharmProject/face-clustering/encodings.pickle'
JOBS = -1

# load the serialized face encodings + bounding box locations from
# disk, then extract the set of encodings to so we can cluster on
# them
print("[INFO] loading encodings...")
data = pickle.loads(open(ENCODINGS_PATH, "rb").read())
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

num = 0
num_of_face = 0
newpath = '/Users/taanhtuan/Desktop/PycharmProject/face-clustering/Data/data'

# loop over the unique face integers
for labelID in labelIDs:
	# find all indexes into the `data` array that belong to the
	# current label ID, then randomly sample a maximum of 25 indexes
	# from the set
	print("[INFO] faces for face ID: {}".format(labelID))
	idxs = np.where(clt.labels_ == labelID)[0]
	print(labelID, ": ")
	print(len(idxs))
	num += len(idxs)
	num_of_face += 1
	num_of_image = 0
	#idxs = np.random.choice(idxs, size=min(25, len(idxs)),replace=False)
	facepath = newpath + str(num_of_face)
	try:
		# Create target Directory
		os.mkdir(facepath)
		print("Directory ", facepath, " Created ")
	except FileExistsError:
		print("Directory ", facepath, " already exists")


	# initialize the list of faces to include in the montage
	faces = []

	# loop over the sampled indexes
	for i in idxs:
		# load the input image and extract the face ROI
		image = cv2.imread(data[i]["imagePath"])
		(top, right, bottom, left) = data[i]["loc"]
		face = image[top:bottom, left:right]
		num_of_image += 1

		# force resize the face ROI to 96x96 and then add it to the
		# faces montage list
		face = cv2.resize(face, (175,175))
		cv2.imwrite(facepath + '/' + str(num_of_image) + '.jpg', face)
		#faces.append(face)

	#print(len(faces))
	# create a montage using 96x96 "tiles" with 5 rows and 5 columns
	#montage = build_montages(faces, (90, 90), (60, 60))[0]

	# show the output montage
	#title = "Face ID #{}".format(labelID)
	#title = "Unknown Faces" if labelID == -1 else title
	#cv2.imshow(title, montage)
	#cv2.waitKey(0)

print(num)