#%%
import pickle,os
import numpy as np
import matplotlib.pyplot as plt
#%%
dir1=os.listdir("G:\\platform-tools\\data_extracted")
ptr=[open("G:\\platform-tools\\data_extracted\\"+i,"rb") for i in dir1]
data=[pickle.load(i) for i in ptr]
#%%

for i in data:
    temp=[]
    for j in range(0,len(i)):
        if(i[j]==1):
            temp.append(i[j])
            temp.append(i[j-1])
    for j in temp:
        i.remove(j)
#%%
def f1(data,s):
    idata1=[data[i] for i in range(0,len(data)) if(i%2==1)]
    ndata=[data[i] for i in range(0,len(data)) if(i%2==0)]
    temp=[]
    for idata in idata1:
        a=[]
        for i in range(0,len(idata[0])):
            a.append(idata[0][i]*idata[1][i]*0.5)
        temp.append(a)
    main=[]
    if(len(temp)==len(ndata)):
        for i in range(0,len(ndata)):
            main.append(ndata[i])
            main.append(temp[i])
    with open("G:\\platform-tools\\main\\"+s,"wb") as f:
        pickle.dump(main,f)
for i in range(0,len(data)):
    f1(data[i],dir1[i])

    