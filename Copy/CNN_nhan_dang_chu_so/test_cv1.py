import tensorflow as tf
import cv2


# Returns a compiled model identical to the previous one
model = tf.keras.models.load_model('model.h5')

img_test = cv2.imread('anh7.png', 0)
img_test = img_test.reshape(1, 28, 28, 1)
img_test = tf.cast(img_test, tf.float32)
print(model.predict(img_test))