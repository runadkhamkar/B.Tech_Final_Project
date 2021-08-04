import concurrent.futures
import time
import os
import sys
import dlib
import cv2
import time
import os,glob
import threading
import math
import matplotlib.pyplot as plt


detector = dlib.get_frontal_face_detector()
predictor_path = r'shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(predictor_path)
data=[]

def t1(str1):
    print(str1)
    cam=cv2.VideoCapture(str1)
    count=0
    temp=[]
    lstpt=[48,50,52,54,56,58]
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
    h1=[]
    h2=[]
    h3=[]
    h4=[]
    for i in temp:
        c=[]
        c.append(i[0])
        c.append(i[3])
        m=(c[1][1]-c[0][1])/(c[1][0]-c[0][0])
        c=-(m*c[1][0])+c[1][1]
        h1.append(abs(m*i[1][0]-i[1][1]+c)/math.sqrt(m**2+1))
        h2.append(abs(m*i[5][0]-i[5][1]+c)/math.sqrt(m**2+1))
        h3.append(abs(m*i[2][0]-i[2][1]+c)/math.sqrt(m**2+1))
        h4.append(abs(m*i[4][0]-i[4][1]+c)/math.sqrt(m**2+1))
    d.append(h1)
    d.append(h2)
    d.append(h3)
    d.append(h4)
    if(len(d)==4):
        return d
    else:
        return 1

def f1():
    dir1=[]
    os.chdir('H:\Project\s7')
    for f in glob.glob("*.mpg"):
        dir1.append(f)
    print("length of data:",len(dir1))
    st=time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        g = {executor.submit(t1, dir1[i]): dir1[i] for i in range(0,10)}
    for i in concurrent.futures.as_completed(g):
        data.append(i.result())
    ft=time.time()
    print(ft-st)


if __name__=="__main__":
    f1()
    print(len(data))
    with open("s7.txt","w") as f:
        for i in data:
            f.write("%s\n"%i)
    
        