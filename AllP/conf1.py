#%%
import concurrent.futures
import time
import os,pickle
import sys
import dlib
import cv2
import time
import os,glob
import threading
import math
import matplotlib.pyplot as plt
import numpy as np

#%%
detector = dlib.get_frontal_face_detector()
predictor_path = r'shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor('C:\\Users\\mllab\\Downloads\\Documents\\shape_predictor_68_face_landmarks.dat')
data=[]

def t1(str1):
    print(str1)
    cam=cv2.VideoCapture(str1)
    count=0
    temp=[]
    lstpt=[51,57]
    while True:
        ret_val, img = cam.read()
        if(ret_val==False):
            break
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        dets = detector(rgb_image,1)
        temp2=[]
        for k, d in enumerate(dets):
            shape = predictor(img, d)
            count+=1
            for i in lstpt:
                temp1=[]
                temp1.append(shape.part(i).x)
                temp1.append(shape.part(i).y)
                temp2.append(temp1)
        temp.append(temp2)
    cv2.destroyAllWindows()
    d=[]
    for i in temp:
        if(len(i)!=2):
            return str1,1
    	a=math.sqrt((i[0][0]-i[1][0])**2+(i[0][1]-i[1][1])**2)
    	d.append(round(a,2))
	
    if(len(d)==75):
    	return str1,d
    else:
        return str1,1
#%%
name=[]
def f1():
    dir1=[]
    os.chdir('s5')
    for f in glob.glob("*.mpg"):
        dir1.append(f)
    print("length of data:",len(dir1))
    st=time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        g = {executor.submit(t1, dir1[i]): dir1[i] for i in range(0,len(dir1))}
    for i in concurrent.futures.as_completed(g):
        a,b=i.result()
        data.append(a)
        data.append(b)
    ft=time.time()
    print(ft-st)

#%%
if __name__=="__main__":
    f1()
    print(len(data))
    with open("C:\\Users\\mllab\\Downloads\\Documents\\s5op2.txt","wb") as file:
        pickle.dump(data,file)
    
        