import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

def score(X,y,k=7,p=2,q=2,r=2):
	X = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0)) #min max scale by feature
	nbrs = NearestNeighbors(n_neighbors=k+1).fit(X)
	distances, indices = nbrs.kneighbors(X)
	distances = distances[:,1:]
	indices = indices[:,1:]
	classes = y[indices] # class by neighbord
	yMatrix = np.transpose(np.array([list(y)]*k)) #class matrix
	scMatrix = (yMatrix == classes)*1 #same class matrix [1 same class, 0 diff class]
	dcMatrix = (scMatrix)*(-1)+1 #different class matrix [negation of scMatrix] 
	dt = np.transpose(distances) #Normalizing distances between neighbords 
	nd = (dt - dt.min(axis=0)) / ( (dt.max(axis=0) - dt.min(axis=0)) +0.001 ) #Normalizing distances between neighbords
	nd = np.round(np.transpose(nd),2) #Normalizing distances between neighbords
	scd = distances*scMatrix #Same class distance
	dcd = distances*dcMatrix #Different class distance
	scnd = nd*scMatrix #Same class normalized distance
	dcnd = nd*dcMatrix #Different class normalized distance
	#Lambda computation
	plamb = (1 - scnd)*scMatrix
	lamb = (dcnd + plamb)
	lambs = np.sum(lamb,axis=1)
	#lambs2 = np.round(((lambs/max(lambs))**(1/p)),2)
	lambs2 = np.round(((lambs/max(lambs))**(1/p)),2)
	lambr = round(sum(lambs2)/len(y),2)
	#print(lambs2)
	#print(lambr)
	#omega
	#Not used
	#gamma
	gamma = round(sum((np.sum(scMatrix,axis=1)/k)**(1/p))/len(y),2)
	#print("lambda, gamma: ",lambr,gamma)
	return round((lambr + gamma)/2,2)

'''
#print(lambs2)
#print(lambr)
print("mask")
print(scMatrix[0:3])
print(dcMatrix[0:3])
print("dist")
print(distances[0:3])
print(nd[0:3])
print("res")
print(dcnd[0:3])
print(scnd[0:3])
print(plamb[0:3])
print("lamb")
print(lamb[0:3])
print(np.sum(lamb,axis=1))
'''
