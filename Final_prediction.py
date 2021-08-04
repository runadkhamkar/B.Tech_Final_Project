#%%
import sys
import dlib
import cv2,pickle
import time
import os,glob
import threading
import math
import matplotlib.pyplot as plt
import numpy as np
from python_speech_features import mfcc


#%%
detector = dlib.get_frontal_face_detector()
predictor_path ='G:\\platform-tools\\shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(predictor_path)
data=[]
spe=input("Enter the speaker:")
path="G:\\platform-tools\\"+spe+"\\"
#path="G:\\platform-tools\\bbil1n.mpg"
inpt=input("Enter the video name:")
str1=path+"\\"+inpt+".mpg"
cam=cv2.VideoCapture(str1)
st=time.time()
temp=[]
lstpt=[51,57,48,54]
win = dlib.image_window()
while True:
    ret_val, img = cam.read()
    if(ret_val==False):
        break
    rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dets = detector(rgb_image,1)
    temp2=[]
    win.clear_overlay()
    win.set_image(img)
    for k, d in enumerate(dets):
        shape = predictor(img, d)
        for i in lstpt:
            temp1=[]
            temp1.append(shape.part(i).x)
            temp1.append(shape.part(i).y)
            temp2.append(temp1)
            win.add_overlay(shape)
    win.add_overlay(dets)
    temp.append(temp2)
    #temp.append(temp2)
    if cv2.waitKey(1) == 1:
        break
cv2.destroyAllWindows()
#%%
d=[]
for i in temp:
    a=math.sqrt((i[0][0]-i[1][0])**2+(i[0][1]-i[1][1])**2)
    b=math.sqrt((i[2][0]-i[3][0])**2+(i[2][1]-i[3][1])**2)
    d.append(int(0.5*a*b))
#%%

path="G:\\platform-tools\\Align1\\"+spe+"\\"
#path="G:\\platform-tools\\bbil1n.align"
file=path+"\\"+inpt+".align"
with open(file,"r") as f:
    R=f.readlines()
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
start=[int(math.ceil(i/1000)) for i in start]
T=[[int(i) for i in j[1]]for j in X]
End=[]
for i in T:
    s=0
    for j in i:
        s=s*10+j
    End.append(s)
End=[int(math.ceil(i/1000)-1) for i in End]
L=[[i for i in j[2]]for j in X]
lett=[]
for i in L:
    l=""
    for j in i:
        if(j!="\n"):
            l=l+str(j)
    lett.append(l)
data=[]
for i in range(0,len(lett)):
    if(lett[i]!='sil'):
        tp=d[start[i]:End[i]]
        data.append(tp)
lett=lett[1:-1]

ldata=[]
for i in data:
    while(len(i)!=20):
        i.append(0)
#%%
print("Original:",lett)
print("Predicting data in grand models:")
classifier=pickle.load(open("G:\\platform-tools\\Grand.pickle","rb"))
print("classified text:",classifier.predict(data))
#%%
print("Classification of data in different models:")
dir1=os.listdir("G:\\platform-tools\\Models")
M=[]
for i in dir1:
    M.append(pickle.load(open("G:\\platform-tools\\Models\\"+i,"rb")))
pre=[]
count=0
for i in data:
   temp=[]
   for j in M:
       temp.append(j.predict([i]))
   pre.append(temp)
for i in pre:
    print("Original:",lett[count])
    temp=[]
    for j in i:
        if(j[0] not in temp):
            temp.append(j[0])
    score=[]
    total=0
    for j in temp:
        c=i.count(j)
        total+=c
        score.append(c)
    Final={}
    for j in range(0,len(score)):
        Final[temp[j]]=score[j]
    for a,b in sorted(Final.items()):
        print(a,b)
    print("Total score of",lett[count],"is:",Final[lett[count]])
    count+=1
    print(">>>>>>>>>>>>>>>>>>>>>>")     