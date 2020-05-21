import numpy as np
import time 
from random import shuffle


f = lambda W: svm_loss_naive(W, X, y, .1)[0]

# for checking if calculated grad is correct
def numerical_grad_general(W, f):
    eps = 1e-6
    g = np.zeros_like(W)
    # flatening variable -> 1d. Then we need 
    # only one for loop
    W_flattened = W.flatten()
    g_flattened = np.zeros_like(W_flattened)
    
    for i in range(W.size):
        W_p = W_flattened.copy()
        W_n = W_flattened.copy()
        W_p[i] += eps 
        W_n[i] -= eps 
        
        # back to shape of W 
        W_p = W_p.reshape(W.shape)
        W_n = W_n.reshape(W.shape)
        g_flattened[i] = (f(W_p) - f(W_n))/(2*eps)
        
    # convert back to original shape
    return g_flattened.reshape(W.shape) 

# this should be very small

# naive way to calculate loss and grad
def svm_loss_naive(W, X, y, reg):
    d, C = W.shape 
    _, N = X.shape 
    
    ## naive loss and grad
    loss = 0 
    dW = np.zeros_like(W)
    for n in range(N):
        xn = X[:, n]
        score = W.T.dot(xn)
        for j in range(C):
            if j == y[n]: 
                continue  
            margin = 1 - score[y[n]] + score[j]
            if margin > 0:
                loss += margin 
                dW[:, j] += xn 
                dW[:, y[n]] -= xn
    
    loss /= N 
    loss += 0.5*reg*np.sum(W * W) # regularization
    
    dW /= N 
    dW += reg*W # gradient off regularization 
    return loss, dW
    
# more efficient way to compute loss and grad
def svm_loss_vectorized(W, X, y, reg,it):
    
    d, C = W.shape 
    _, N = X.shape 
    loss = 0 
    dW = np.zeros_like(W)
    
    Z = W.T.dot(X)

    correct_class_score = np.choose(y, Z).reshape(N,1).T     
    margins = np.maximum(0, Z - correct_class_score + 1) 
    l = margins.shape[1]
    if it == 100:
        print()
        print()
        print(it," : ")
        print(Z)
        print()
        print(correct_class_score)
        print()
        print(y)
        print(np.arange(l))
        print()
        print(margins)
    margins[y, np.arange(l)] = 0
    if it == 100: 
        print()
        print(margins)
        print()
    
    loss = np.sum(margins, axis = (0, 1))
    loss /= N
    loss += 0.5 * reg * np.sum(W * W)
    
    F = (margins > 0).astype(int)
    if it == 100:
        print("F : ")
        print(F)
        print()
    F[y, np.arange(l)] = np.sum(-F, axis = 0)
    dW = X.dot(F.T)/N + reg*W 

    if it == 100:
        print("F : ")
        print(F)
        print()
        print(dW) 


    return loss, dW

# Mini-batch gradient descent
def multiclass_svm_GD(X, y, Winit, reg, lr=.1, batch_size = 100, num_iters = 1000, print_every = 100):
    batch_size = 5
    W = Winit 
    loss_history = np.zeros((num_iters))
    for it in range(num_iters):
        # randomly pick a batch of X
        idx = np.random.choice(X.shape[1], batch_size)
        X_batch = X[:, idx]
        y_batch = y[idx]

        loss_history[it], dW = svm_loss_vectorized(W, X_batch, y_batch, reg,it)

        W -= lr*dW 
        #if it % print_every == 1:
        #    print("it ", it,"/",num_iters," loss = ", loss_history[it])

    return W, loss_history




N, C, d = 20, 3, 2
#49000, 3, 10
reg = .1 
W = np.random.randn(d, C)
X = np.random.randn(d, N)
y = np.random.randint(C, size = N)



#t1 = time.time()
#l1, dW1 = svm_loss_naive(W, X, y, reg)
#t2 = time.time()
#print('Naive     : run time:', t2 - t1, '(s)')

#t1 = time.time()
#l2, dW2 = svm_loss_vectorized(W, X, y, reg)


#t2 = time.time()

#print('Vectorized: run time:', t2 - t1, '(s)')
#print('loss difference:', np.linalg.norm(l1 - l2))
#print('gradient difference:', np.linalg.norm(dW1 - dW2))

W, loss_history = multiclass_svm_GD(X, y, W, reg)

print()
print()
print(W.T)



