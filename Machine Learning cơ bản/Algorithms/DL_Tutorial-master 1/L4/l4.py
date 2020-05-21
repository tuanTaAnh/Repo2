# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:37:33 2019

@author: DELL
"""

# Thêm thư viện
import numpy as np
import pandas as pd

# Hàm sigmoid
def sigmoid(x):
        return 1/(1+np.exp(-x))
 
   
# Đạo hàm hàm sigmoid
def sigmoid_derivative(x):
        return x*(1-x)


# Lớp neural network
class NeuralNetwork:
    def __init__(self, layers, learning_rate=0.1):
	    # Mô hình layer ví dụ [2,2,1]
        #print(len(layers))
        self.layers = layers 
      
        # Hệ số learning rate
        self.learning_rate = learning_rate
            
        # Tham số W, b
        self.W = []
        self.b = []
        
        # Khởi tạo các tham số ở mỗi layer
        for i in range(0, len(layers)-1):
            w_ = np.random.randn(layers[i], layers[i+1])
            b_ = np.zeros((layers[i+1], 1))
            self.W.append(w_/layers[i])
            self.b.append(b_)
    
	
	# Train mô hình với dữ liệu
    def update_dW2(self, x, y,epoch):
        A = [x]
        
        #quá trình feedforward
        out = A[-1]
        for i in range(0, len(self.layers) - 1):
            g1 = np.dot(out, self.W[i])
            g2 = (self.b[i].T)
            g3 = g1 + g2
            out = sigmoid(g3)
            A.append(out)
    
        a = y
        y = y.reshape(-1, 1)
            #if epoch == 10: print(y)
        dA = [-(y/A[-1] - (1-y)/(1-A[-1]))]
        dW = []
        db = []

        for i in reversed( range( 0, len(self.layers)-1 ) ):
            dw_ = np.dot((A[i]).T, dA[-1] * sigmoid_derivative(A[i+1]))
            db_ = (np.sum(dA[-1] * sigmoid_derivative(A[i+1]), 0)).reshape(-1,1)
            dA_ = np.dot(dA[-1] * sigmoid_derivative(A[i+1]), self.W[i].T)

            dW.append(dw_)
            db.append(db_)
            dA.append(dA_)

        # Đảo ngược dW, db
        dW = dW[::-1]
        db = db[::-1]

        # Gradient descent
        for i in range(0, len(self.layers)-1):
            #if epoch == 10: print(i) 
            self.W[i] = self.W[i] - self.learning_rate * dW[i]
            self.b[i] = self.b[i] - self.learning_rate * db[i]
      

    def training_data2(self,X,y):
        for epoch in range(10000):
            if epoch%200 == 0: print(epoch)
            self.update_dW2(X,y,epoch)

    def predict(self,X,y):
        A1 = X
        A2 = sigmoid(np.dot(A1,self.W[0])+self.b[0].T)
        A3 = sigmoid(np.dot(A2,self.W[1])+self.b[1])
        
        Y_predict = A3

        """
        for i in range(len(y)):
            print(Y_predict[i]," ",y[i])
        
        print() 
        """

        for i in range(len(y)):
            if Y_predict[i] < 0.5: Y_predict[i] = 0
            else: Y_predict[i] = 1

        """
        for i in range(len(y)):
            print(Y_predict[i]," ",y[i])
        """

        print('training accuracy: %.2f' % (np.mean(Y_predict == y))) 

        
# Dataset bài 2
data = pd.read_csv('/Users/taanhtuan/Desktop/DL_Tutorial-master 1/L4/dataset.csv').values
N, d = data.shape
X = data[:, 0:d-1].reshape(-1, d-1)
y = data[:, 2].reshape(-1, 1)

print(1e-0)
print(0.1)
#q = NeuralNetwork([2,2,1],0.1)
#q.training_data2(X,y)
#q.predict(X,y)

"""
a = np.array([[1,1,1],[2,2,2],[3,3,3]])
c = a*(1-a)

print(a)
print()
print() 
print(1-a)
print()
print() 
print(c)


[[ 3.62739053 -0.78289284]
 [ 1.77092401 -0.66334997]
 [ 2.14221732 -0.68725854]
 [ 2.53061912 -0.6024057 ]
 [ 2.86769542 -0.84383711]
 [ 3.27605715 -0.63209594]
 [ 1.37681937 -0.78445662]
 [ 1.75666693 -0.75398448]
 [ 2.89620959 -0.66256808]
 [ 1.39107645 -0.6938221 ]
 [ 2.92187235 -0.49942595]
 [ 2.55485617 -0.44832702]
 [ 1.43384771 -0.42191855]
 [ 1.80514102 -0.44582713]
 [ 2.55057904 -0.47551737]
 [ 1.43384771 -0.42191855]
 [ 1.81369527 -0.39144642]
 [ 2.18498857 -0.41535499]
 [ 2.55343046 -0.45739047]
 [ 2.92044664 -0.5084894 ]]

[[ 0.00744497 -0.01191411]]

[[ 3.6348355  -0.79480695]
 [ 1.77836898 -0.67526408]
 [ 2.14966228 -0.69917265]
 [ 2.53806409 -0.61431981]
 [ 2.87514039 -0.85575122]
 [ 3.28350212 -0.64401005]
 [ 1.38426434 -0.79637073]
 [ 1.76411189 -0.76589859]
 [ 2.90365456 -0.67448219]
 [ 1.39852142 -0.70573621]
 [ 2.92931731 -0.51134006]
 [ 2.56230113 -0.46024113]
 [ 1.44129268 -0.43383266]
 [ 1.81258598 -0.45774124]
 [ 2.55802401 -0.48743148]
 [ 1.44129268 -0.43383266]
 [ 1.82114023 -0.40336053]
 [ 2.19243354 -0.4272691 ]
 [ 2.56087543 -0.46930458]
 [ 2.9278916  -0.52040351]]
"""
