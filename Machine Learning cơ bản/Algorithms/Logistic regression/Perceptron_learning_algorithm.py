# generate data
# list of points 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
np.random.seed(2)

def h(w, x):    
    return np.sign(np.dot(w.T, x))

def has_converged(X, y, w):    
    return np.array_equal(h(w, X), y) 

def perceptron(X, y):
    d = X.shape[0]
    w = np.random.randn(d, 1)
    N = X.shape[1]
    d = X.shape[0]
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
     
        if has_converged(X, y, w): break



    return (w, mis_points)


means = [[2, 2], [4, 2]]
cov = [[.3, .2], [.2, .3]]
N = 10
X0 = np.random.multivariate_normal(means[0], cov, N).T
X1 = np.random.multivariate_normal(means[1], cov, N).T

X = np.concatenate((X0, X1), axis = 1)
y = np.concatenate((np.ones((1, N)), -1*np.ones((1, N))), axis = 1)
# Xbar 
X = np.concatenate((np.ones((1, 2*N)), X), axis = 0)

(w, m) = perceptron(X, y)


print()
print()
print()
print(w[-1])
print()
print(m) 
print()
print()
print()