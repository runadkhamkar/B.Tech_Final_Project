import pickle,os,sys
import matplotlib.pyplot as plt
from hmmlearn.hmm import GaussianHMM as Gh
import numpy as np
from python_speech_features import mfcc


with open("ds71.txt","rb") as f:
	temp=pickle.load(f)
data=[i[1:-1] for i in temp if(i[0]!='sp')]

X=[]
for i in data:
	temp=np.array([])
	for j in i:
		if(len(temp)==0):
			temp=j
		else:
			temp=np.append(temp,j,axis=0)
	X.append(temp)
models=[]
def build(data):
    model=Gh(n_components=30,covariance_type="diag",n_iter=1000)
    m1=model.fit(data)
    models.append(m1)
for i in range(0,51):
    build(X[i])
    print(i)