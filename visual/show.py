import sys
import pickle
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d


def text_display(text):
    return ''.join([chr(int(t)) for t in text if t != 0])


def onpick(event):
    ind = event.ind
    print 'scatter: {} {} {}'.format(ind[0], text_display(Xtrain[ind[0]].A1), Ytrain[ind[0]])


if len(sys.argv) < 2:
    print "Enter the file you want to show"
    sys.exit()


# Load filename
filename = sys.argv[1]


with open(filename, "rb") as f:
    reduced = pickle.load(f)
    Xtrain = pickle.load(f)
    Ytrain = pickle.load(f)


fig = plt.figure()


# Build the subgraph
if "3D" in filename:
    ax1 = fig.add_subplot(111, projection = "3d")
    col = ax1.scatter(reduced[:,0], reduced[:,1], reduced[:,2], s=100, c=Ytrain, alpha=0.5, picker=True)
else:
    ax1 = fig.add_subplot(111)
    col = ax1.scatter(reduced[:,0], reduced[:,1], s=100, c=Ytrain, alpha=0.5, picker=True)


fig.canvas.mpl_connect('pick_event', onpick)
plt.show()