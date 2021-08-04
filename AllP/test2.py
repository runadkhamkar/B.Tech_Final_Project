#%%
import pickle
import os
from python_speech_features import mfcc
import numpy as np
models=[]
#l=os.listdir("G:\\platform-tools")
models=pickle.load(open("2594.5.txt","rb"))
with open("G:\platform-tools\ds71.txt","rb") as f:
	dump=pickle.load(f)
dump=[i for i in dump if(i[0]!='sp')]
#data=[i[1:] for i in dump if(i[0]!='sp')]
#%%
with open("testdata.txt","rb") as f:
	data=pickle.load(f)
#%%
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
				print("predict:",dump[i][0],ld[i],"\n")
				name.append(dump[i][0])
				ld.remove(ld[i])
				break
	return name
for i in data:
    f=mfcc(np.array(i),500)
    #print("Original",dump[i][0])
    a=test(f,1)
    

#%%
