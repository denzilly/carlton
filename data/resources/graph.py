import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


data=pd.read_csv("data/training_data/train_converted_label.csv").as_matrix()
clf = DecisionTreeClassifier()


xtrain = data[0:500,1:]
train_label = data[0:500,0]

clf.fit(xtrain,train_label)

xtest = data[500:,1:]
test_label = data[500:,0]


test = 1

d=xtrain[test]
d.shape=(28,28)
pt.imshow(255-d,cmap='gray')
pt.show()
print(train_label[test])
