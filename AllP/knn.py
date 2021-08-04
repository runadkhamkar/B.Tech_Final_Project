#%%
import os,pickle,random
from sklearn.neighbors import KNeighborsClassifier
dir1=os.listdir("G:\platform-tools\Final")
X_train=[]
y_train=[]
for inpt in dir1:
    data=pickle.load(open("G:\\platform-tools\\Final\\"+inpt,"rb"))
    
    for i in data:
        label=i[0]
        for j in i[1:]:
            X_train.append(j)
            y_train.append(label)
print(len(X_train),len(y_train))
classifier = KNeighborsClassifier(n_neighbors=1)  
classifier.fit(X_train, y_train)  
pre=classifier.predict(X_train)
c=0
for i in range(0,len(y_train)):
    if(y_train[i]==pre[i]):
        c+=1
#%%
        print("Model:",classifier)
A=round(c/len(X_train),4)
print("Accuracy:",A*100)

