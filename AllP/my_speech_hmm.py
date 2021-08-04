import os
import numpy as np
from scipy.io import wavfile
from python_speech_features import mfcc
import matplotlib.pyplot as plt
import random
from hmmlearn.hmm import GaussianHMM as Gh
path="C:\\Users\\hp\\audio\\audio"
os.chdir(path)
sub=os.listdir()
data=[]
for i in sub:
    temp=[]
    temp=os.listdir(i)
    data.append(temp)
print(len(data),len(data[0]),data[0][0])
files=[]
freqs=[]
for i in range(0,len(data)):
    temp0=np.array([])
    for j in range(0,len(data[i])):
        file=str(path)+"\\"+str(sub[i])+"\\"+str(data[i][j])
        files.append(file)
        x,y=wavfile.read(file)
        freq=mfcc(y,x)
        if(len(temp0)==0):
            temp0=freq
            continue
        temp0=np.append(temp0,freq,axis=0)
    freqs.append(temp0)
models=[]
def build(data):
    model=Gh(n_components=4,covariance_type="diag",n_iter=1000)
    m1=model.fit(data)
    models.append(m1)
u=int(input("Enter Total number of classes(upto 7):"))
for i in range(0,u):
    build(freqs[i])
print("Total models build:",len(models))
print("Classes:")
for i in range(0,u):
    print(sub[i])
def score1(model,data):
    s=model.score(data)
    return s
score1(models[0],freq)
def test(data):
    a,b=wavfile.read(data)
    y=mfcc(b,a)
    scp=[]
    for i in range(0,len(models)):
        sc=score1(models[i],y)
        scp.append(sc)
    #print(scp)
    x=max(scp)
    for i in range(0,len(scp)):
        if(scp[i]==x):
            print("Original:",data,"\nPridicted:",sub[i])
print("Test case:")
test(str(path)+"\\"+str(sub[2])+"\\"+str(data[2][0]))
n=int(input("Enter number of tests:"))
for i in range(0,n):
    j=random.randint(0,6)
    k=random.randint(0,6)
    test(str(path)+"\\"+str(sub[j])+"\\"+str(data[j][k]))