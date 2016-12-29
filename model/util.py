import numpy as np
import pandas as pd

from sklearn.utils import shuffle

def get_seperate(train):
    """ Get seperate data form to fill in sklearn function
    @param train: train data must be in a zipped list
    
    @returns: datas and its labels
    """
    

    Xtrain = []
    Ytrain = []
    for t in train:
        Xtrain.append(t[0])
        Ytrain.append(t[1])
    
    Xtrain = np.matrix(Xtrain)
    return Xtrain, Ytrain


def text_display(text):
    return ''.join([chr(int(t)) for t in text if t != 0])


def getRanData(filename, number=0, shuffle=1):
    """ Get Data from Ransomware
    @param number : this number indicates how many lines of data you want to extract
           shuffle: set 1 to shuffle the origin data, else not.
    
    @returns: data and its labels
    """
    

    file_in = filename + ".in"
    file_out = filename + ".out"
    

    # Ransomware payload data:
    # column 0-1499 is data, with values 0 .. 255
    xtrain = pd.read_csv(file_in, header=None).as_matrix().astype(np.float32)
    ytrain = pd.read_csv(file_out, header=None).values.flatten().tolist()
    

    if not shuffle:
        if number: 
            train = zip(xtrain[:number], ytrain[:number])
        else: 
            train = zip(xtrain, ytrain)
    else:
        # shuffle the matrix
        if number: 
            train = shuffle(zip(xtrain[:number], ytrain[:number]))
        else: 
            train = shuffle(zip(xtrain, ytrain))

    Xtrain, Ytrain = get_seperate(train)

    return Xtrain, Ytrain