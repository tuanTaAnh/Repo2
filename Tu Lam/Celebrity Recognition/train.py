from DataLoad.loaddata import MasterImage
from cnnmodel.model import CNNNet
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

EPOCHS = 300
INIT_LR = 1e-3
BS = 32
validationRatio = 0.15
IMAGE_DIMS = (175, 175, 3)
path = '/Users/taanhtuan/Desktop/PycharmProject/Celebrity Recognition/FaceData'

a = MasterImage(PATH=path, Height = IMAGE_DIMS[0], Width = IMAGE_DIMS[1])
data,labels = a.load_dataset()
list_of_classes = a.get_categories()
num_of_classes = len(list_of_classes)

print(data.shape)
print(labels.shape)

(X_train, X_validation, y_train, y_validation) = train_test_split(data, labels, test_size=validationRatio, random_state=42)

# Hien thi loi
assert(X_train.shape[0]==y_train.shape[0]), "The number of images in not equal to the number of lables in training set"
assert(X_validation.shape[0]==y_validation.shape[0]), "The number of images in not equal to the number of lables in validation set"
assert(X_train.shape[1:]==((IMAGE_DIMS[1], IMAGE_DIMS[0], IMAGE_DIMS[2])))," The dimesions of the Training images are wrong "
assert(X_validation.shape[1:]==(IMAGE_DIMS[1], IMAGE_DIMS[0], IMAGE_DIMS[2]))," The dimesionas of the Validation images are wrong "

model = CNNNet.build(
		width=IMAGE_DIMS[0],
		height=IMAGE_DIMS[1],
		depth=IMAGE_DIMS[2],
		classes=num_of_classes
	)

model.summary()

opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
model.compile(
		optimizer=opt,
		loss="categorical_crossentropy",
		metrics=["accuracy"]
	)


# construct the image generator for data augmentation
dataGen = ImageDataGenerator(
	rotation_range=25,
	width_shift_range=0.1,
	height_shift_range=0.1,
	shear_range=0.2,
	zoom_range=0.2,
	horizontal_flip=True,
	fill_mode="nearest")

dataGen.fit(X_train)

y_train = to_categorical(y_train,num_of_classes)
y_validation = to_categorical(y_validation,num_of_classes)
print("Num of Classes",num_of_classes)

# train the network
print("[INFO] training network...")
history = model.fit_generator(
		dataGen.flow(X_train, y_train, batch_size=BS),
		validation_data=(X_validation, y_validation),
		steps_per_epoch=len(data) // BS,
		epochs=EPOCHS,
		verbose=1
	)

model.save("model.h5")


