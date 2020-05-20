from loaddata.loaddataset import MasterImage
from HOG.hog import HOG
from HOG.implement import FeatureExtraction
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from sklearn.naive_bayes import MultinomialNB
from keras.preprocessing import image
from PIL import ImageTk, Image
from os import listdir
from os.path import isfile, join
from sklearn.model_selection import KFold, train_test_split

EPOCHS = 300
INIT_LR = 1e-3
BS = 32
height, width = 48, 40

path = '/Users/taanhtuan/Desktop/PycharmProject/ML project/Tu lam/Celebrities regconition/Dataset'

#dictionary to label all traffic signs class.
classes = { 1:'mohamed salah',
            2:'leonardo dicaprio',
            3:'donald trump'}


def classify(file_path):
    global label_packed
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (height, width))
    vector = FeatureExtraction.hog(img)
    test = np.array([vector])
    pred = clf.predict(test)[0]
    sign = classes[pred + 1]
    print("Predict: ",sign)
    label.configure(foreground='#011638', text=sign)


def show_classify_button(file_path):
    classify_b = Button(top, text="Classify Image", command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


a = MasterImage(PATH=path, Height = height, Width = width)

trainX,trainY = a.load_dataset()
list_of_classes = a.get_categories()
num_of_classes = len(list_of_classes)

print(trainX.shape)
print(trainY.shape)

data = np.asarray(HOG.get_data_output(trainX))
print(data.shape)

## call MultinomialNB
clf = MultinomialNB()
# training
clf.fit(data, trainY)

# initialise GUI
top = tk.Tk()
top.geometry('800x600')
top.title('Celebrity Recognition')
top.configure(background='#CDCDCD')

label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)

upload = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))

upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Know Your Traffic Sign", pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')

heading.pack()
top.mainloop()