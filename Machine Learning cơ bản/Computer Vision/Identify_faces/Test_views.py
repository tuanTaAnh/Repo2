import numpy as np 
import matplotlib.pyplot as plt
from sklearn import linear_model 
from sklearn.metrics import accuracy_score
from scipy import misc      # for 
from matplotlib.pyplot import imread
from sklearn import preprocessing
np.random.seed(1)

def build_list_fn(pre, img_ids, view_ids):
    # hàm số để tạo ra tên cho ảnh
    """
    pre = 'M-' or 'W-'
    img_ids: indexes of images
    view_ids: indexes of views
    """
    list_fn = []
    for im_id in img_ids:
        for v_id in view_ids:
            fn = path + pre + str(im_id).zfill(3) + '-' + \
                str(v_id).zfill(2) + '.bmp'
            list_fn.append(fn)
    return list_fn 

def rgb2gray(rgb):
    # Y' = 0.299 R + 0.587 G + 0.114 B 
    return rgb[:,:,0]*.299 + rgb[:, :, 1]*.587 + rgb[:, :, 2]*.114

# feature extraction 
def vectorize_img(filename):    
    # tải ảnh lên, bản chất là 1 ma trận chứa các giá trị pixel 
    rgb = imread(filename)
    # convert to gray scale 
    gray = rgb2gray(rgb)
    # vectorization each row is a data point 
    im_vec = gray.reshape(1, 183923)
    
    return im_vec  

def build_data_matrix(img_ids, view_ids):
    # 
    total_imgs = img_ids.shape[0]*view_ids.shape[0]*2
        
    X_full = np.zeros((total_imgs, 183923))
    y = np.hstack((np.zeros((int(total_imgs/2), )), np.ones((int(total_imgs/2), ))))
    
    list_fn_m = build_list_fn('M-', img_ids, view_ids)
    list_fn_w = build_list_fn('W-', img_ids, view_ids)
    list_fn = list_fn_m + list_fn_w

    print("= = = = = = = = = = = = = = = =")
    print()

    for i in range(len(list_fn)):
        print(i," ",list_fn[i])
        X_full[i, :] = vectorize_img(list_fn[i])

    print()
    print("= = = = = = = = = = = = = = = =")
    print()
    print()

    X = np.dot(X_full, ProjectionMatrix)
    return (X, y)

def feature_extraction(X):
    return (X - x_mean)/x_var  

def feature_extraction_fn(fn):
    im = vectorize_img(fn)
    im1 = np.dot(im, ProjectionMatrix)
    return feature_extraction(im1)



path = '/Users/taanhtuan/Desktop/Machine learning co ban/Identify_faces/data/AR/' # path to the database 

train_ids = np.arange(1, 2)
test_ids = np.arange(2, 3)
#view_ids = np.hstack((np.arange(1, 8), np.arange(14, 21)))
view_ids = np.arange(1,3)

D = 165*120 # original dimension 
d = 500 # new dimension 

# generate the projection matrix 
ProjectionMatrix = np.random.randn(183923,112) 

(X_train_full, y_train) = build_data_matrix(train_ids, view_ids)
x_mean = X_train_full.mean(axis = 0)
x_var  = X_train_full.var(axis = 0)

X_train = feature_extraction(X_train_full)
X_train_full = None ## free this variable 

logreg = linear_model.LogisticRegression(C=1e5) # just a big number 
logreg.fit(X_train, y_train)
(X_test_full, y_test) = build_data_matrix(test_ids, view_ids)
X_test = feature_extraction(X_test_full)
X_test_full = None 

y_pred = logreg.predict(X_test)
print("Accuracy: %.2f %%" %(100*accuracy_score(y_test, y_pred)))
print()
print()


fn1 = path + 'M-001-01.bmp'
fn2 = path + 'W-001-01.bmp'
fn3 = path + 'M-001-02.bmp'
fn4 = path + 'W-001-02.bmp'

x1 = feature_extraction_fn(fn1)
p1 = logreg.predict_proba(x1)
print(p1)

x2 = feature_extraction_fn(fn2)
p2 = logreg.predict_proba(x2)
print(p2)

x3 = feature_extraction_fn(fn3)
p3 = logreg.predict_proba(x3)
print(p3)

x4 = feature_extraction_fn(fn4)
p4 = logreg.predict_proba(x4)
print(p4)
