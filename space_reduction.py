import random
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import umap
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn import preprocessing
import icnn

def normalize(X):
    scaler = MinMaxScaler()
    scaler.fit(X)
    return scaler.transform(X)

def evplot(Xp,y,k=11,p=1,q=1,r=1):
    neigh = KNeighborsClassifier(n_neighbors=7)
    neigh.fit(Xp, y)
    icnnscore = icnn.score(Xp,y,k,p,q,r)
    neigscore = round(neigh.score(Xp,y),2)
    fscore = np.round((icnnscore+neigscore)/2,2)
    print("graph score", fscore)
    return round((icnnscore + neigscore)/2,3)



def umapTransfromData(X,y,dim=3):
    reducer = umap.UMAP(random_state=42, transform_seed=42, n_components=dim)
    reducer.fit(X)
    return reducer.transform(X)
     

def umapICNNTransfromData(X,y,dim=3):
    #UMAP NO SUPERVISADO
    #metrics = ["euclidean", "manhattan", "chebyshev", "minkowski"]#, "mahalanobis"]
    metrics = ["euclidean", "manhattan"]#, "mahalanobis"]
    nn = [3,7,17,42]
    bestScore = 0
    worstScore = 1
    tested = []
    for i in range(50):
        m = random.choice(metrics)
        n = random.choice(nn)
        if([m,n] in tested):
            #print("skip:",m,n)
            continue
        tested.append([m,n])
        #print("Current test: ",i,m,n)
        reducer = umap.UMAP(random_state=42, transform_seed=42, n_components=dim, metric=m, n_neighbors=n)
        reducer.fit(X)
        X2 = reducer.transform(X)
        #print("=======================")
        score = evplot(X2,y)
        if(score > bestScore):
            bestScore = score
            bestParams = [m,n]
            XB = X2.copy()
    return XB

def dataPrePro(dataset):
    df=pd.read_csv(dataset)
    #df=df.drop(df.index[0:1])
    df = df.sample(frac=1, random_state=42) #Shuffle rows
    data = df.values
    #data = data[0:500,:]
    X = data[:,2:]
    classes = data[:,0]
    le = preprocessing.LabelEncoder()
    le.fit(classes)
    y = le.transform(classes)
    limg = list(data[:,1]) 
    X = normalize(X)
    return X,y,classes,le,limg