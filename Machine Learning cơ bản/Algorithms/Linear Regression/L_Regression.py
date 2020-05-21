
import numpy as np
import pandas as pd
from sklearn import linear_model

def read_data(csv_file):
    csv_df = pd.read_csv(csv_file)
    return csv_df

def split_data(csv_df):
    input = csv_df.iloc[:, :-1] # lấy trên mọi hàng, và chỉ bỏ cột cuối cùng
    output = csv_df.iloc[:, -1] # lấy trên mọi hàng, và chỉ lấy cột cuối cùng
    x = input.values
    y = output.values.reshape((-1, 1)) # reshape để chuyển y thành ma trận cột
    return x, y

def find_optimize(input, outcome):
    """
    input.T: chuyển vị của ma trận input
    np.dot(a,b) : nhân từng phần tử của ma trận a với ma trận b
    np.linalg.pinv(x): tìm giả ngịch đảo/ ngịch đảo của ma trận x
    """
    w = np.dot(np.linalg.pinv(np.dot(input.T, input)), np.dot(input.T, outcome))
    return w

def optimize_with_sklearn(input, outcome):
    regr = linear_model.LinearRegression(fit_intercept=False)  # fit_intercept = False for calculating the bias
    regr.fit(input, outcome)
    return regr.coef_

def get_loss_value(input, outcome, w):
    cost = 0
    y_hat = np.dot(input, w)
    for x, y in zip(outcome, y_hat):
        print('Outcome:', x[0], 'Predict:', y[0])
        cost += pow(x[0] - y[0], 2)
    return cost / 2

def predict_new_data(input, w):
    # convert to input_bar
    one = np.ones((input.shape[0], 1))
    input = np.concatenate((one, input), axis=1)
    return np.dot(input, w)

# chuyển ma trận input sang ma trận input bar
# bằng cách thêm vector cột giá trị 1 vào trước ma trận
one = np.ones((input.shape[0], 1))
input = np.concatenate((one, input), axis=1)
w1 = find_optimize(input, outcome)
w2 = optimize_with_sklearn(input, outcome)
print(w1.T) # chuyển vị ma trận
print(w2)
