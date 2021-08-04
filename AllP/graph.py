#%%
import pickle,os
import matplotlib.pyplot as plt
import concurrent.futures as cf
#%%
data1=pickle.load(open("G:\platform-tools\s1up1.txt","rb"))
data2=pickle.load(open("G:\platform-tools\s1up1.txt","rb"))
#%%
def UP():
path="G:\\platform-tools\\graph\\up\\"
with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
    g = {executor.submit(t1, data1[i]): data1[i] for i in range(0,len(data1))}
for i in concurrent.futures.as_completed(g):
	a,b=i.result()
for i in data1:
    label=i[0]
    count=0
    print(label,len(i))
    for j in i[1:]:
        plt.plot(j)
        plt.axis(")
        plt.savefig(path+label+str(count)+".png")
        plt.clf()
        count+=1
#%%
path="G:\\platform-tools\\graph\\side\\"
for i in data1:
    label=i[0]
    count=0
    print(label,len(i))
    for j in i[1:]:
        plt.plot(j)
        plt.savefig(path+label+str(count)+".png",cmap='gray')
        plt.clf()
        count+=1
        