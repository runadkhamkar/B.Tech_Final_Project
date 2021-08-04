#%%
import pickle,os
import numpy as np
#%%
dir1=os.listdir("G:\\platform-tools\\data_extracted")
ptr=[open("G:\\platform-tools\\data_extracted\\"+i,"rb") for i in dir1]
data=[pickle.load(i) for i in ptr]
#%%
for inpt in data:
    temp=[]
    for i in range(0,len(inpt)):
        if(i%2==0):
            temp.append(inpt[i])
            continue
        for j in range(0,len(inpt[1][0])):
            a=inpt[i][0][j]*inpt[i][1][j]
            temp.append(a)