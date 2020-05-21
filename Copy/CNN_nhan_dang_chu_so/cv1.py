import cv2
import tensorflow as tf
from keras.utils import np_utils
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.models import Sequential
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)

x_train = x_train.astype('float32')

x_train /= 255
y_train = np_utils.to_categorical(y_train, 10)

#mạng CNN
model = Sequential([
    Conv2D(filters=32, kernel_size=(3, 3), input_shape=(28, 28, 1), activation = tf.nn.relu),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(filters=32, kernel_size=(3, 3), activation = tf.nn.relu),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(300, activation=tf.nn.relu),
    Dense(10, activation=tf.nn.softmax),
])

model.compile(optimizer='sgd', loss='mean_squared_error',metrics=['accuracy'])
#model.summary()

model.fit(x_train, y_train, epochs=5)

model.save('model.h5')

img_test = cv2.imread('anh9.png', 0) #ảnh của số 9
cv2.imshow('anh test', img_test)
cv2.waitKey(0)
img_test = img_test.reshape(1, 28, 28, 1)

img_test = tf.cast(img_test, tf.float32)
print(model.predict(img_test))

img_test = cv2.imread('anh4.png', 0) #ảnh của số 4
cv2.imshow('anh test', img_test)
cv2.waitKey(0)
img_test = img_test.reshape(1, 28, 28, 1)

img_test = tf.cast(img_test, tf.float32)
print(model.predict(img_test))