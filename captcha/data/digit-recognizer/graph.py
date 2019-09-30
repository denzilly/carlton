import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


data=pd.read_csv("train_converted1.csv").as_matrix()
clf = DecisionTreeClassifier()


xtrain = data[0:80,1:]
train_label = data[0:80,0]

clf.fit(xtrain,train_label)


xtest = data[80:,1:]
actual_label = data[80:,0]

p = clf.predict(xtest)

print(p)
print(actual_label)
