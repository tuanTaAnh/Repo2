# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt

# height (cm)
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
Y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T
 
xich_ma_x = 0
xich_ma_x_y = 0
xich_ma_x_2 = 0
xich_ma_y = 0

height_X, weight_X = X.shape
height_Y, weight_Y = Y.shape
n = height_X

for y in range(0,height_Y):
    xich_ma_y += Y[i][0]
for i in range(0,height_X):
    xich_ma_x += X[i][0]
for i in range(0,height_X):
    xich_ma_x_2 += X[i][0]*X[i][0]
for i in range(0,height_X):
    xich_ma_x_y += X[i][0]*Y[i][0]

w_0 = (xich_ma_x_2*xich_ma_y - xich_ma_x*xich_ma_x_y)/(n*xich_ma_x_2 - xich_ma_x*xich_ma_x)

w_1 = (xich_ma_x*xich_ma_y - n*xich_ma_x_y)/(xich_ma_x*xich_ma_x - n*xich_ma_x_2)

print()
print(w_0, " ", w_1)
print()
