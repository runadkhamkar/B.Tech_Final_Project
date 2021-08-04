#%%
import pickle,os,sys,random
import matplotlib.pyplot as plt
from hmmlearn.hmm import GaussianHMM as Gh
import numpy as np
from python_speech_features import mfcc


with open("G:\platform-tools\s1up.txt","rb") as f:
	dump=pickle.load(f)
dump=[i for i in dump if(i[0]!='sp')]
data=[i[1:] for i in dump if(i[0]!='sp')]
#data=[i[:38] for i in data]
dump[:5]
#%%
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
#%%
from hmmlearn.hmm import GaussianHMM as Gh
M=[]
ncl=[20,25]
for nc in ncl:
	models=[]
	print("Total internal steps:",nc)
	def build(data):
	    model=Gh(n_components=nc,covariance_type="diag",n_iter=1000)
	    m1=model.fit(data)
	    models.append(m1)
	for i in range(0,len(X)):
	    build(X[i])
	print("Total models build:",len(models))
	M.append(models)
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
	for b in range(1,2):
		count=0
		total=0
		for i in range(0,len(X)):
			total+=1
            m=random.randint(0,51)
            n=random.randint(0,10)
			f=mfcc(np.array(data[m][0]),500)
			#print("Original:",dump[i][0])
			a=test([f],b)
			if(dump[i][j] in a):
				count+=1
		print("Total Accuracy is",(count/total)*100)

#%%
os.chdir("G:\platform-tools")
with open("2594.5.txt","wb") as f:
    pickle.dump(M[1],f)
	