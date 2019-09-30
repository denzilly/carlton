import pyscreenshot as ImageGrab
import time
from selenium import webdriver
import image_slicer
from PIL import Image
import os

from csvconverter_slices import img_to_csv

import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


#os.chdir("/home/bart/programming/carlton")

print (os.getcwd())
### This function collects the captcha, and splits it into 6 separate images, eacht with a neutral gray background




def predict_captcha():
    training_data = pd.read_csv("data/training_data/train_converted_label.csv").as_matrix()
    testing_data = pd.read_csv("data/captcha_slices/testdata.csv").as_matrix()
    clf = DecisionTreeClassifier()


    xtrain = training_data[:600,1:]
    train_label = training_data[:600,0]

    clf.fit(xtrain,train_label)


    xtest = training_data[400:,1:]
    test_label = training_data[400:,0]

    captcha = testing_data[:,1:]



    p = clf.predict(captcha)
    captcha = ""
    for x in p:
        captcha += str(x)

    print(captcha)
    return captcha


def solve_captcha():

    img_to_csv()
    captcha = predict_captcha()

    return captcha