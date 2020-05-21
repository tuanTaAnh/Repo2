# generate data
# list of points 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
np.random.seed(2)

def h(w, x):    
    return np.sign(np.dot(w.T, x))

def has_converged(X, y, w):    
    return np.array_equal(h(w, X), y) 

def perceptron(X, y):

    N = X.shape[1]
    d = X.shape[0]
    #w = np.random.randn(d, 1)
    w = np.full((d,1),0.1)
    mis_points = []

    while True:
        # mix data 
        mix_id = np.random.permutation(N)
        for i in range(N):
            xi = X[:, mix_id[i]].reshape(d, 1)
            yi = y[0, mix_id[i]]
            if h(w, xi)[0] != yi: # misclassified point
                mis_points.append(mix_id[i])
                w = w + yi*xi 
        
        if has_converged(X, y,w):
            break
    return (w, mis_points)


data = pd.read_csv("dataset.csv").values
# lay chieu dai chieu rong cua bo du lieu
N, d = data.shape

x = data[:, 0:d-1].reshape(-1,d-1).T
y = data[:, d-1].reshape(-1, 1).T 

x = np.concatenate((np.ones((1, N)), x), axis = 0)


(w, m) = perceptron(x, y)
print(w) 
