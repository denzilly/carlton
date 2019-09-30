from captcha import collect_slices
from csvconverter_slices import img_to_csv

import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


collect_slices()
img_to_csv()


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

print(p)

#count = 0
#for i in range(0,200):
#    count += 1 if p[i]==test_label[i] else 0
#print(count)
#print("accuracy=", (count/200)*100)
