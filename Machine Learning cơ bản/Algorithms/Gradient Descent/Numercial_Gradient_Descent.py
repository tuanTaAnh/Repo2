# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
np.random.seed(2)

X = np.random.rand(1000, 1)
y = 4 + 3 * X + .2*np.random.randn(1000, 1) # noise added

# Building Xbar 
one = np.ones((X.shape[0],1))
Xbar = np.concatenate((one, X), axis = 1)


def grad(w):
    N = Xbar.shape[0]
    return 1/N * np.dot(Xbar.T,np.dot(Xbar,w) - y)

def cost(w):
    N = Xbar.shape[0]
    
    return 0.5/N * np.linalg.norm( y - np.dot(Xbar,w), 2 )**2 # ** mũ 

def numerical_grad(w, cost):
    eps = 1e-4
    g = np.zeros_like(w)
    w_p = w.copy()
    w_n = w.copy()
    for i in range(len(w)):
        w_p[i] += eps 
        w_n[i] -= eps
        g[i] = (cost(w_p) - cost(w_n))/(2*eps)
        print("+ ",g[i])
    return g

def check_grad(w, cost, grad):
    w = np.random.rand(w.shape[0], w.shape[1])
    grad1 = grad(w)
    grad2 = numerical_grad(w, cost)
    return True if np.linalg.norm(grad1 - grad2) < 1e-6 else False 


A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w_lr = np.dot(np.linalg.pinv(A), b)
print(Xbar)
print(np.linalg.pinv(A))
print('Solution found by formula: w = ',w_lr.T)

print( 'Checking gradient...', check_grad(np.random.rand(2, 1), cost, grad))
