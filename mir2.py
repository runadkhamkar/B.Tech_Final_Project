#%%
import sys
import dlib
import cv2
import time
import os,glob
import threading
import math,pickle
import matplotlib.pyplot as plt


#%%
detector = dlib.get_frontal_face_detector()
predictor_path = r'shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(predictor_path)
lstpt=[51,57,48,54]
data=[]
labels=[["begin","choose","connection","navigation","next","previous","start","stop","hello","web"],["stop navigation","excuse me","i am sorry","thank you","good bye","i love this game","nice to meet you","you are welcome","how are you","have a goog time"]]
#%%
path="G:\\platform-tools\\Miracle"
dir1=os.listdir(path)
for i in dir1:
    print(i)
    #speaker
    path=path+"\\"+i
    dir2=os.listdir(path)
    for j in dir2:
        #words/phrases
        if(j=='words'):
            ind=0
        else:
            ind=1
        path1=path
        path=path+"\\"+j
        dir3=os.listdir(path)
        for k in dir3:
            print(k)
            #id
            tp=int(k)-1
            l=labels[ind][tp]
            path2=path
            path=path+"\\"+k
            dir4=os.listdir(path)
            
            for m in dir4:
                data.append(l)
                #instance
                temp=[]
                path3=path
                path=path+"\\"+m
                dir5=os.listdir(path)
                for n in dir5:
                    if(n[0]=='d'):
                        continue
                    file=path+"\\"+n
                    print(file)
                
                    img = cv2.imread(file,0)
                    rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    dets = detector(rgb_image,1)
                    temp2=[]
                    for k, d in enumerate(dets):
                        shape = predictor(img, d)
                        A=d.left()
                        B=d.top()
                        C=d.right()
                        D=d.bottom()
                        d1=D-B
                        d2=C-A
                        area=d1*d2
                        for z in lstpt:
                            temp1=[]
                            temp1.append(shape.part(z).x)
                            temp1.append(shape.part(z).y)
                            temp2.append(temp1)
                    #print(temp2)
                    a=math.sqrt((temp2[0][0]-temp2[1][0])**2+(temp2[0][1]-temp2[1][1])**2)
                    b=math.sqrt((temp2[2][0]-temp2[3][0])**2+(temp2[2][1]-temp2[3][1])**2)
                    temp.append(a*b*0.5/area)
                    
                path=path3
                data.append(temp)
                print("\n",len(temp),temp,"\n")
            path=path2
        path=path1
    path="G:\\platform-tools\\Miracle"
    pickle.dump(data,open("G:\\platform-tools\\Miracle"+i+".txt","wb"))
#%%
pickle.dump(data,open("G:\\platform-tools\\MiracleF01.txt","wb"))