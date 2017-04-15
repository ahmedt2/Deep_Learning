import scipy.io as sio
import numpy as np
import sklearn
from matplotlib import pyplot as plt
from math import e
from math import log
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sys import maxsize
from scipy import stats
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.preprocessing import OneHotEncoder

data = sio.loadmat("letters_data.mat") #/Users/AhmedThabet/Desktop/school/189/HOMEWORK/HW5/spam_ham/
X = data['train_x']
y = data['train_y']
tst = data['test_x']


X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=43)

def test_clf(pred, orig):
    m = []
    for i in range(len(pred)):
        if pred[i] == orig[i]:
            m.append(1)
    res = len(m)/len(pred)
    if res > 0.72:
        print("SUCESS!!!")
    else:
        print("Failure....")
    return res


import time
from sklearn.neural_network import MLPClassifier
# clf = MLPClassifier(hidden_layer_sizes=(1000, 400), activation='tanh', warm_start=True)
# clf = MLPClassifier(hidden_layer_sizes=(400), activation='relu', solver = 'sgd', learning_rate='adaptive',warm_start=True)
clf = MLPClassifier(hidden_layer_sizes=(1000, 500, 200, 100), warm_start=True)
st = time.clock()
clf.fit(X_train, y_train.reshape((len(y_train))))
end = time.clock()
print(int((-st + end)//60), "+", (((-st + end)/60)%1)*60)
print(test_clf(y_test, clf.predict(X_test))*100)
