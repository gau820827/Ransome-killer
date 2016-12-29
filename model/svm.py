import pickle
import numpy as np

from sklearn.model_selection import cross_val_score, train_test_split
from sklearn import svm
from sklearn.utils import shuffle

from util import get_seperate


""" Sample input
filename = "./packetData/Cryptwall/packet_pcainfo"
"""

# Read reduced data
filename = raw_input()

with open(filename, "rb") as f:
    reduced = pickle.load(f)
    Xtrain = pickle.load(f)
    Ytrain = pickle.load(f)


# Shuffle data
xtrain, ytrain = get_seperate(shuffle(zip(reduced, Ytrain)))


# Pick first 10 dimensions to train
reduced = 10


# linear SVM + 5-folds Cross Validation
clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, xtrain[:, :reduced], ytrain, cv=5)
print "poly-3 scores: {}".format(scores)


# poly-3 SVM + 5-folds Cross Validation
clf = svm.SVC(kernel='poly', degree=3, C=1)
scores = cross_val_score(clf, xtrain[:, :reduced], ytrain, cv=5)
print "poly-3 scores: {}".format(scores)


# poly-4 SVM + 5-folds Cross Validation
clf = svm.SVC(kernel='poly', degree=4, C=1)
scores = cross_val_score(clf, xtrain[:, :reduced], ytrain, cv=5)
print "poly-4 scores: {}".format(scores)
