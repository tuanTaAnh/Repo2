from __future__ import print_function
import numpy as np 
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from cvxopt import matrix, solvers
np.random.seed(22)

means = [[2, 2], [4, 2]]
cov = [[.3, .2], [.2, .3]]
N = 10
X0 = np.random.multivariate_normal(means[0], cov, N) # class 1
X1 = np.random.multivariate_normal(means[1], cov, N) # class -1 
X = np.concatenate((X0.T, X1.T), axis = 1) # all data 
y = np.concatenate((np.ones((1, N)), -1*np.ones((1, N))), axis = 1) # labels 


#build P
V = np.concatenate((X0.T, -X1.T), axis = 1)
P = matrix(np.dot(V.T,V)) # see definition of V, K near eq (8)


#print((V.T.dot(V)).shape) 
#print()
#print(K)

q = matrix(-np.ones((2*N, 1))) # all-one vector 
#build A, b, G, h
G = matrix(-np.eye(2*N)) # for all lambda_n >= 0
h = matrix(np.zeros((2*N, 1)))
A = matrix(y) #the equality constrain is actually y^T lambda = 0
b = matrix(np.zeros((1, 1))) 

print(np.zeros((2*N, 1)).shape)

solvers.options['show_progress'] = False
sol = solvers.qp(P, q, G, h, A, b) #Quadratic Programming 

"""
x = argmin 1/2 * x.T * K * x + q.T * x (+ r) 
subject to: 
            G * x <= h
            A * x = b
"""

l = np.array(sol['x'])
#print('lambda = ')
#print(l.T)


epsilon = 1e-6 #just a small number, greater than 1e-9
S = np.where(l > epsilon)[0]

VS = V[:, S]
XS = X[:, S]
yS = y[:, S]
lS = l[S]
# calculate w and b
w = np.dot(VS,lS)
b = np.mean(yS.T - np.dot(w.T,XS))

print('w = ', w.T)
print('b = ', b)