from keras.models import Sequential
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from sklearn.model_selection import train_test_split
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Dense
from keras import backend as K
from loaddata.loaddataset import MasterImage

EPOCHS = 300
INIT_LR = 1e-3
BS = 32
(height, width, depth) = (150, 150, 3)

path = '/Users/taanhtuan/Desktop/PycharmProject/ML project/Test Demo/dataset'
a = MasterImage(PATH=path, IMAGE_DIMS = (height, width, depth))

data,labels = a.load_dataset()
list_of_classes = a.get_categories()
num_of_classes = len(list_of_classes)

(trainX, testX, trainY, testY) = train_test_split(data, labels, test_size=0.15, random_state=42)

print(data.shape)
print(labels.shape)


if K.image_data_format() == 'channels_first':
    input_shape = (depth, height, width)
else:
    input_shape = (height, width, depth)

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', # or categorical_crossentropy
              optimizer='rmsprop',# or adagrad
              metrics=['accuracy'])

model.fit(trainX, trainY, batch_size = 32, epochs = 100)

'''
# performing data argumentation by training image generator
dataAugmentaion = ImageDataGenerator(
    rotation_range = 30,
    zoom_range = 0.20,
    fill_mode = "nearest",
    shear_range = 0.20,
    horizontal_flip = True,
    width_shift_range = 0.1,
    height_shift_range = 0.1)

# training the model
model.fit_generator(
    dataAugmentaion.flow(trainX, trainY, batch_size = 32),
    validation_data = (testX, testY),
    steps_per_epoch = len(trainX) // 32,
    epochs = 10)


inputShape = (height, width, depth)
chanDim = -1

# if we are using "channels first", update the input shape
# and channels dimension
if K.image_data_format() == "channels_first":
    inputShape = (depth, height, width)
    chanDim = 1

# initialize the model along with the input shape to be
model = Sequential()

# CONV => RELU => POOL
model.add(Conv2D(32, (3, 3), padding="same", input_shape=inputShape))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(3, 3)))
model.add(Dropout(0.25))

# (CONV => RELU) * 2 => POOL
model.add(Conv2D(64, (3, 3), padding="same"))
model.add(Activation("relu"))
model.add(Conv2D(64, (3, 3), padding="same"))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# (CONV => RELU) * 2 => POOL
model.add(Conv2D(128, (3, 3), padding="same"))
model.add(Activation("relu"))
model.add(Conv2D(128, (3, 3), padding="same"))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# first (and only) set of FC => RELU layers
model.add(Flatten())

model.add(Dense(1024))
model.add(Activation("relu"))

# softmax classifier
model.add(Dense(num_of_classes))
model.add(Activation("softmax"))

opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
model.compile(
		optimizer=opt,
		loss="categorical_crossentropy",
		metrics=["accuracy"]
	)

dataAugmentaion = ImageDataGenerator(
    rotation_range = 30,
    zoom_range = 0.20,
    fill_mode = "nearest",
    shear_range = 0.20,
    horizontal_flip = True,
    width_shift_range = 0.1,
    height_shift_range = 0.1)


model.fit_generator(
    dataAugmentaion.flow(trainX, trainY, batch_size = 32),
    validation_data = (testX, testY), 
    steps_per_epoch = len(trainX) // 32,
    epochs = 10)
'''



