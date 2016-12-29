import pickle
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d


from util import getRanData, text_display


from sklearn.decomposition import PCA
from sklearn.manifold import TSNE


def tsne_divide(tsne, reduced, length, divide=5):
    # Divide and conquer
    length = len(Ytrain)
    times = length/divide
    last = length%divide
    for i in xrange(5):
        if i == 0:
            # First vectors
            Z = tsne.fit_transform(reduced[i*times:(i+1)*times, :reduce_number])
        elif i == length-1:
            # The last vectors
            Z = np.concatenate((Z,
                    tsne.fit_transform(reduced[i*times:last, :reduce_number])))
        else:
            Z = np.concatenate((Z,
                    tsne.fit_transform(reduced[i*times:(i+1)*times, :reduce_number])))
    return Z


def twoDB(Xtrain, Ytrain):

    
    pca = PCA()
    reduced = pca.fit_transform(Xtrain)


    tsne = TSNE()
    Z = tsne_divide(tsne, reduced, len(Ytrain))


    # Save the PCA vectors
    with open("packet_tsneBinfo"+str(reduce_number), "wb") as f:
        pickle.dump(Z, f)
        pickle.dump(Xtrain, f)
        pickle.dump(Ytrain, f)
    
    return
    

def threeDB(Xtrain, Ytrain):

        
    pca = PCA()
    reduced = pca.fit_transform(Xtrain)

    tsne = TSNE(n_components=3)
    Z = tsne_divide(tsne, reduced, len(Ytrain))

    
    # Save the PCA vectors
    with open("packet_3DtsneBinfo"+str(reduce_number), "wb") as f:
        pickle.dump(Z, f)
        pickle.dump(Xtrain, f)
        pickle.dump(Ytrain, f)
    
    return


if __name__ == '__main__':
    
    filename = "./packet/Cryptmic/small_train"
    
    reduce_number = int(raw_input())
    Xtrain, Ytrain = getRanData(filename, number=20, shuffle=0)
    twoDB(Xtrain, Ytrain)
    threeDB(Xtrain, Ytrain)