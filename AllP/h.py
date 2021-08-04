import pickle,os,sys
import matplotlib.pyplot as plt
from hmmlearn.hmm import GaussianHMM as Gh
import numpy as np
from python_speech_features import mfcc


with open("ds7.txt","rb") as f:
	temp=pickle.load(f)
dataa=[i[1:-1] for i in temp if(i[0]!='sp')]
#data=[i[:38] for i in data]
X=[]
for i in dataa:
    x=np.array([])
    for j in i:
        if(len(j)==0):
            continue
        f=mfcc(np.array(j),5000)
        if(len(x)==0):
            x=f
        else:
            x=np.append(x,f,axis=0)
    X.append(x)
from hmmlearn.hmm import GaussianHMM as Gh
d=dataa[0:100]
models=[]
def build(dataa):
    model=Gh(n_components=20,covariance_type="diag",n_iter=1000)
    m1=model.fit(dataa)
    models.append(m1)
for i in range(0,51):
    build(X[i])
    print(i)
print("Total models build:",len(models))
def score1(model,dataa):
    s=model.score(dataa)
    return s
for i in models:
	print(score1(i,X[1]))