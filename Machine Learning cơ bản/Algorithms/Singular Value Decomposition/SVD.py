import numpy as np
from numpy import linalg as LA

m, n = 2, 3
A = np.random.rand(m, n)

U, S, V = LA.svd(A)

# checking if U, V are orthogonal and S is a diagonal matrix with
# nonnegative decreasing elements
print( 'Frobenius norm of (UU^T - I) =', LA.norm(U.dot(U.T) - np.eye(m)))

print( '\n U = ', U.shape, '\n')
print( '\n U = ', U, '\n')

print( '\n S = ', S.shape, '\n')
print( '\n S = ', S, '\n')

print( '\n V = ', V.shape, '\n')
print( '\n V = ', V, '\n')

print( 'Frobenius norm of (VV^T - I) =', LA.norm(V.dot(V.T) - np.eye(n)))