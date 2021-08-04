#%%
import pickle,os
import matplotlib.pyplot as plt
import concurrent.futures
#%%
data1=pickle.load(open("G:\\platform-tools\\Final\\s1.txt","rb"))
#data2=pickle.load(open("G:\platform-tools\s1side1.txt","rb"))
#%%
def t1(i):
    path="G:\\platform-tools\\graph1\\up\\"
    label=i[0]
    count=0
    l=[]
    for j in i[1:]:
        if(j==0):
            break
        l.append(j)
    #print(label,len(i))
    plt.plot(j)
    plt.axis('off')
    plt.savefig(path+label+str(count)+".png")
    plt.clf()

def t2(i):
    path="G:\\platform-tools\\graph1\\side\\"
    label=i[0]
    count=0
    print(label,len(i))
    for j in i[1:]:
        plt.plot(j)
        plt.axis('off')
        plt.savefig(path+label+str(count)+".png")
        plt.clf()
        count+=1


def UP():
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        g = {executor.submit(t1, data1[i]): data1[i] for i in range(0,len(data1))}

def SIDE():
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        g = {executor.submit(t2, data2[i]): data2[i] for i in range(0,len(data2))}
#%%
if __name__=="__main__":
    UP()
    #SIDE()
        