import numpy as np 
## One-hot coding
from scipy import sparse
#from scipy.special import softmax

# randomly generate data 
N = 2 # number of training sample 
d = 2 # data dimension 
C = 3 # number of classes 


def softmax(Z):
    """
    Compute softmax values for each sets of scores in V.
    each column of V is a set of score.    
    """
    e_Z = np.exp(Z)
    A = e_Z / e_Z.sum(axis = 0)
    
    return A

def convert_labels(y, C = C):
    """
    convert 1d label to a matrix label: each column of this 
    matrix coresponding to 1 element in y. In i-th column of Y, 
    only one non-zeros element located in the y[i]-th position, 
    and = 1 ex: y = [0, 2, 1, 0], and 3 classes then return

            [[1, 0, 0, 1],
             [0, 0, 1, 0],
             [0, 1, 0, 0]]
    """
    Y = sparse.coo_matrix( ( np.ones_like(y), (y, np.arange(len(y)) ) ) , shape = ( C, len(y) ) ).toarray()

    return Y

# cost or loss function  
def cost(X, Y, W):
    
    A = softmax(np.dot(W.T,X)) # W.T.dot(X) = np.dot(W.T,X)
    return -np.sum(Y*np.log(A))

def grad(X, Y, W):
    A = softmax(np.dot(W.T,X))
    E = A - Y
    
    return np.dot(X,E.T)

def numerical_grad(X, Y, W, cost):
    eps = 1e-6
    g = np.zeros_like(W)
    print(W)
    print()
    for i in range(W.shape[0]):
        for j in range(W.shape[1]):
            W_p = W.copy()
            W_n = W.copy()
            print(i," ",j," : ",W_p[i, j]+0.000001," ",W_n[i,j]-0.000001)
            print(eps)
            W_p[i, j] = W_p[i, j] + eps
            W_n[i, j] = W_n[i, j] - eps
            print(W_p[i, j]," ",W_n[i, j])
            g[i,j] = (cost(X, Y, W_p) - cost(X, Y, W_n))/(2*eps)

    return g


#X = np.random.randn(d, N)
#y = np.random.randint(0, 3, (N,)) 
#Y = convert_labels(y, C)
#W_init = np.random.randn(d, C)

X = np.array([[ 0.03904431,  0.43196035 ], [ -0.8607632,  -0.70698798 ]])
y = [ 2, 2 ]
Y = convert_labels(y, C)


#W_init = np.array([[-0.55233328, -1.53049112,  0.30089727], [-1.23243331, -1.91960346, -0.89818812]])
W_init = np.array([[1, 1, 1],[1, 1, 1]])

g1 = grad(X, Y, W_init)
g2 = numerical_grad(X, Y, W_init, cost)


print("+")
print(g1)
print("+")
print(g2)
print("+")

print(np.linalg.norm(g1 - g2))

