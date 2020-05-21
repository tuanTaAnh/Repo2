# import libraries
import numpy as np
import pandas as pd




#Hàm sigmoid
def sigmoid(x):
        return 1/(1+np.exp(-x))
 
#Đạo hàm hàm sigmoid
def sigmoid_derivative(x):
        return x*(1-x)


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
    

    def update_dW(self,X,y,epoch):
        A1 = X
        A2 = sigmoid(np.dot(A1,self.W[0])+self.b[0].T)
        A3 = sigmoid(np.dot(A2,self.W[1])+self.b[1])
        
        Y_predict = A3

        
        dw_2 = np.dot((A2.T),Y_predict - y)
        db_2 = (-1*np.sum(Y_predict - y)).reshape(-1,1)

        dw_1 = np.dot( (X.T) , np.dot((Y_predict - y),(self.W[1].T)) * sigmoid_derivative(A2) )
        db_1 = (np.sum( np.dot((Y_predict - y),(self.W[1].T)) * sigmoid_derivative(A2), 0) ).reshape(-1,1)

        dW = []
        db = []

        dW.append(dw_1)
        dW.append(dw_2)

        db.append(db_1)
        db.append(db_2)

        for i in range(len(self.layers)-1):
            self.W[i] = self.W[i] - self.learning_rate*dW[i]
            self.b[i] = self.b[i] - self.learning_rate*db[i]


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
            self.W[i] = self.W[i] - self.learning_rate * dW[i]
            self.b[i] = self.b[i] - self.learning_rate * db[i]
      

    def training_data(self,X,y):
        for epoch in range(10000):
            if epoch%1000 == 0: print(epoch)
            self.update_dW(X,y,epoch)

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
#data = pd.read_csv('/Users/taanhtuan/Desktop/DL_Tutorial-master 1/L4/dataset.csv').values
data = pd.read_csv('dataset.csv').values
N, d = data.shape
X = data[:, 0:d-1].reshape(-1, d-1)
y = data[:, 2].reshape(-1, 1)


p = NeuralNetwork([2,2,1],1e-1)
p.training_data(X,y)
p.predict(X,y)

"""
def update_W(self,dW,db):
        for i in range(len(self.layers)-1):
            self.W[i] = self.W[i] - self.learning_rate*dW[i]
            self.b[i] = self.b[i] - self.learning_rate*db[i]


    def update_dW(self,X,y,epoch):
        A1 = X
        A2 = sigmoid(np.dot(A1,self.W[0])+self.b[0].T)
        A3 = sigmoid(np.dot(A2,self.W[1])+self.b[1])
        
        Y_predict = A3

        
        dw_2 = np.dot((A2.T),Y_predict - y)
        #if epoch%200 == 0: print("+")
        #if epoch%200 == 0: print(dw_2)
        #if epoch%200 == 0: print("+")

        db_2 = (-1*np.sum(Y_predict - y)).reshape(-1,1)

        dw_1 = np.dot( (X.T) , np.dot((Y_predict - y),(self.W[1].T)) * sigmoid_derivative(A2) )
        db_1 = (np.sum( np.dot((Y_predict - y),(self.W[1].T)) * sigmoid_derivative(A2), 0) ).reshape(-1,1)

        dW = []
        db = []

        dW.append(dw_1)
        dW.append(dw_2)

        db.append(db_1)
        db.append(db_2)

        self.update_W(dW,db) 


    def training_data(self,X,y):
        for epoch in range(1):
            self.update_dW(X,y,epoch)

    def update_W2(self,dW,db):
        for i in range(len(self.layers)-1):
            self.W[i] = self.W[i] - self.learning_rate*dW[i]
            self.b[i] = self.b[i] - self.learning_rate*db[i]


    def update_dW2(self,X,y,epoch):

        if epoch%200 == 0: print("+ + + + + + + + + + + + + + +")
        A = [X]
        
        out = A[-1]
        for i in range(0, len(self.layers) - 1):
            g1 = np.dot(out, self.W[i])
            g2 = (self.b[i].T)
            g3 = g1 + g2
            out = sigmoid(g3)
            A.append(out)
        

        a = y
        y = y.reshape(-1, 1)
        dA = [-(y/A[-1] - (1-y)/(1-A[-1]))]
        dW = []
        db = []

        for i in reversed( range( 0, len(self.layers)-1 ) ):
            dw_ = np.dot( (A[i]).T , dA[-1] * sigmoid_derivative(A[i+1]) )
            db_ = (np.sum(dA[-1] * sigmoid_derivative(A[i+1]), 0) ).reshape(-1,1)

            if epoch%200 == 0: print("+")
            if epoch%200 == 0: print(db_)
            if epoch%200 == 0: print("+")

            dA_ = np.dot(dA[-1] * sigmoid_derivative(A[i+1]), self.W[i].T)

            dW.append(dw_)
            db.append(db_)
            dA.append(dA_)
        
        # Đảo ngược dW, db
        dW = dW[::-1]
        db = db[::-1]

        self.update_W2(dW,db) 


    def training_data2(self,X,y):
        for epoch in range(10000):
            self.update_dW2(X,y,epoch)
        print("end")
"""