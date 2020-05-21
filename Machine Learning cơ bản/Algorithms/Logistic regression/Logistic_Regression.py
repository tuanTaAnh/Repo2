# Thêm thư viện
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def logistic_function(x):
    return 1/(1+ np.exp(-x))

def logistic_function_derivative(x,y,w):
    y_predict = logistic_function(np.dot(x,w))
    return np.dot(x.T, y_predict-y)

def check(w,w_moi):
    tol = 1e-4
    if np.linalg.norm(w-w_moi) < tol: return True
    return False 

def Logistic_Regression(x,y):

    w = np.full((d, 1), 0.1)
    learning_rate = 0.01

    while(True):
        w_moi = w - learning_rate*logistic_function_derivative(x,y,w)
        if check(w,w_moi): break
        w = w_moi

    return w



data = pd.read_csv("dataset.csv").values
# lay chieu dai chieu rong cua bo du lieu
N, d = data.shape

x = data[:, 0:d-1].reshape(-1, d-1)
y = data[:, d-1].reshape(-1, 1)

print(x) 

x = np.hstack((np.ones((N, 1)), x))


w = Logistic_Regression(x,y)
print(w) 



