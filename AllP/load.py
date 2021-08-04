import pickle
import os,glob,math
import matplotlib.pyplot as plt
with open("G:\platform-tools\s7op.txt","rb") as f:
	data=pickle.load(f)
rml=[]
for i in range(0,len(data)):
    if(data[i]==1):
        rml.append(data[i])
        rml.append(data[i-1])
for i in rml:
    data.remove(i)
print("Total length of data:",len(data))
dir1=[]
os.chdir('G:\\platform-tools\\align')
for f in glob.glob("*.align"):
    dir1.append(f)
name=[data[i][:-4] for i in range(0,len(data)) if i%2==0]
list1=[data[i] for i in range(0,len(data)) if i%2!=0]
ptr=[]
#print(len(dir1),len(name),dir1)
for i in range(0,len(name)):
	for j in range(0,len(dir1)):
		if(name[i]==dir1[j][:-6]):
			f=open(dir1[j],"r")
			ptr.append(f)
words=[]
for i in ptr:
	words.append(i.readlines())
data1=[]
lett1=[]
count=0
for R in words:
    X=[]
    for i in R:
        X.append([j for j in i.split(" ")])
    T=[[int(i) for i in j[0]]for j in X]
    start=[]
    for i in T:
        s=0
        for j in i:
            s=s*10+j
        start.append(s)
    start=[math.ceil(i/1000) for i in start]
    T=[[int(i) for i in j[1]]for j in X]
    End=[]
    for i in T:
        s=0
        for j in i:
            s=s*10+j
        End.append(s)
    End=[math.ceil(i/1000)-1 for i in End]
    L=[[i for i in j[2]]for j in X]
    lett=[]
    for i in L:
        l=""
        for j in i:
            if(j!="\n"):
                l=l+str(j)
        lett.append(l)
    data=[]
    temp=list1[count]
    count+=1
    for i in range(0,len(lett)):
        if(lett[i]!='sil'):
            tp=temp[start[i]:End[i]]
            data.append(tp)
    lett=lett[1:-1]
    temp1=[]
    for i in range(0,len(data)):
        temp2=[]
        temp2.append(lett[i])
        temp2.append(data[i])
        data1.append(temp2)
dump=[]
for i in data1:
    if(i[0] not in dump):
        dump.append(i[0])
print("different words:",len(dump),"\n",dump)
ldata=[]
for i in dump:
    temp=[]
    temp.append(i)
    for j in data1:
        if(j[0]==i):
            temp.append(j[1])
    ldata.append(temp)
for i in ldata:
    s=0
    for j in i[1:]:
        s+=len(j)
    i.append(s/(len(i)-1))
with open("ds7.txt","wb") as f:
    pickle.dump(ldata,f)