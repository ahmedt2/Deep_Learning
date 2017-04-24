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
import scipy
from scipy.special import expit
import random
import time

data = sio.loadmat("images.mat", mat_dtype=True) #/Users/AhmedThabet/Desktop/school/189/HOMEWORK/HW5/spam_ham/
X = data['images']
_X = X
X = X.reshape((28*28, 60000)).T

class K_Means():
    def __init__(self, k=2, max_iter=10, n_init=10):
        self.k = k
        self.max_iter = max_iter
        self.n_init = n_init
        self.means = np.random.randint(10,size=10)
        self.clusters = {}
    
    def cluster(self, X, means):
        bins  = {}
        _all = []
        temp_mat = np.zeros((60000, 10))
        _all = [np.linalg.norm(X-m, axis = 1) for m in means]
        for i in range(10):
            temp_mat[:,i] = _all[i]
        temp2 = np.argmin(temp_mat, axis = 1)
        i = 0
        for x in X:
            label = temp2[i]
            i+=1
            try:
                bins[label].append(x)
            except KeyError:
                bins[label] = [x]
        return bins
    
    def center(self, clusters):
        opt_means = []
        for k in clusters:
            opt_means.append(np.mean(clusters[k], axis = 0))
        return opt_means
    
    def converged(self, curr_means, trial_means):
        return np.array_equal(curr_means, trial_means)
        
    def fit(self, X):
        curr_means = [X[random.randint(0,len(X))] for i in range(10)]
        trial_means = [X[random.randint(0,len(X))] for i in range(10)]
        it = 0
        while self.converged(curr_means, trial_means) != True and it < self.max_iter:
            curr_means = trial_means
            bins = self.cluster(X, trial_means)
            trial_means = self.center(bins)
            it += 1
            if (it == self.max_iter):
                print(":(")
        self.means = trial_means
        self.clusters = bins