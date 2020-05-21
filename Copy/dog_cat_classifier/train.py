#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K


# dimensions of our images.
img_width, img_height = 150, 150

train_data_dir = 'data/train'
validation_data_dir = 'data/validation'
nb_train_samples = 2000
nb_validation_samples = 800
epochs = 50
batch_size = 16

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

model = Sequential([
                    Conv2D(filters=32, kernel_size=(3, 3), input_shape=input_shape, activation= tf.nn.relu),
                    MaxPooling2D(pool_size=(2, 2)),
                    Conv2D(filters=32, kernel_size=(3, 3), activation= tf.nn.relu),
                    MaxPooling2D(pool_size=(2, 2)),
                    Conv2D(filters=64, kernel_size=(3, 3), activation= tf.nn.relu),
                    MaxPooling2D(pool_size=(2, 2)),
                    Flatten(),
                    Dense(64, activation=tf.nn.relu),
                    Dropout(0.5),
                    Dense(1, activation=tf.nn.sigmoid),
                ])


model.compile(
                loss='binary_crossentropy', # or categorical_crossentropy
                optimizer='rmsprop',# or adagrad
                metrics=['accuracy']
            )

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True )

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale= 1.0 / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

print("++++++\\\\\+++++++++++++++")
print(train_generator.class_indices)
print("++++++\\\\\+++++++++++++++")

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary'
)

print(train_generator)

print("+++++++++++++++++++++++++++++")
model.fit_generator(
                        train_generator,
                        steps_per_epoch = nb_train_samples // batch_size,
                        epochs=epochs,
                        validation_data = validation_generator,
                        validation_steps = nb_validation_samples // batch_size
                    )
print("+++++++++++++++++++++++++++++")

model.save('model.h5')




""""""

""""""