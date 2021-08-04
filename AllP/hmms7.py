import pickle,os,sys
import matplotlib.pyplot as plt
from hmmlearn.hmm import GaussianHMM as Gh
import numpy as np
from python_speech_features import mfcc


with open("ds71.txt","rb") as f:
	dump=pickle.load(f)
dump=[i for i in dump if(i[0]!='sp')]
data=[i[1:] for i in dump if(i[0]!='sp')]
#data=[i[:38] for i in data]
X=[]
for i in data:
    x=np.array([])
    for j in i:
        if(len(j)==0):
            continue
        f=mfcc(np.array(j),500)
        if(len(x)==0):
            x=f
        else:
            x=np.append(x,f,axis=0)
    X.append(x)
from hmmlearn.hmm import GaussianHMM as Gh

ncl=[20]
for nc in ncl:
	models=[]
	print("Total internal steps:",nc)
	def build(data):
	    model=Gh(n_components=nc,covariance_type="diag",n_iter=1000)
	    m1=model.fit(data)
	    models.append(m1)
	for i in range(0,51):
	    build(X[i])
	print("Total models build:",len(models))
	def score1(model,data):
	    s=model.score(data)
	    return s
	def test(data,h):
		count=0
		ld=[]
		name=[]
		for i in models:
			count+=1
			ld.append(i.score(data))
		for j in range(0,h):
			for i in range(0,len(ld)):
				if(ld[i]==max(ld)):
					#print("predict:",dump[i][0],ld[i])
					name.append(dump[i][0])
					ld.remove(ld[i])
					break
		return name
	for j in range(1,4):
		count=0
		total=0
		for i in range(0,len(X)):
			total+=1
			#print("Original:",dump[i][0])
			a=test(X[i],j)
			if(dump[i][0] in a):
				count+=1
		print("Accuracy of taking top ",j," ",(count/total)*100)
	print("\n\n")