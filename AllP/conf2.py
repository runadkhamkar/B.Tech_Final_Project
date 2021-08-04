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
predictor_path = r'G:\\platform-tools\\shape_predictor_68_face_landmarks.dat'
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
        if(len(i)!=6):
            return str1,1
        c=[]
        c.append(i[0])
        c.append(i[3])
        m=(c[1][1]-c[0][1])/(c[1][0]-c[0][0])
        c=-(m*c[1][0])+c[1][1]
        h1.append(round(abs(m*i[1][0]-i[1][1]+c)/math.sqrt(m**2+1),2))
        h2.append(round(abs(m*i[5][0]-i[5][1]+c)/math.sqrt(m**2+1),2))
        h3.append(round(abs(m*i[2][0]-i[2][1]+c)/math.sqrt(m**2+1),2))
        h4.append(round(abs(m*i[4][0]-i[4][1]+c)/math.sqrt(m**2+1),2))
    d.append(h1)
    d.append(h2)
    d.append(h3)
    d.append(h4)
    temp=[]
    for j in range(0,len(d[0])):
        s=0
        for i in d:
            s=s+i[j]
        temp.append(round(s/4,2))
    with open("bbbl8p.align","r") as f:
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
    lett=lett[1:-1]
    if(len(d)==4):
        return str1,d
    else:
        return str1,1

name=[]
def f1():
    dir1=[]
    dir2=[]
    os.chdir('G:\platform-tools\s5')
    for f in glob.glob("*.mpg"):
        dir1.append(f)
    os.chdir("align")
    for f in glob.glob("*.align"):
        dir2.append(f)
    if(len(dir1)!=len(dir2)):
        print("Error")
        sys.exit(-1)
    print("length of data:",len(dir1),len(dir2))
    st=time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        g = {executor.submit(t1, dir1[i]): dir1[i] for i in range(0,4)}
    for i in concurrent.futures.as_completed(g):
        a,b=i.result()
        data.append(a)
        name.append(b)
    ft=time.time()
    print(ft-st)


if __name__=="__main__":
    f1()
    print(len(data))
    with open("G:\platform-tools\s7op1.txt","w") as f:
        for i in range(0,len(data)):
            f.write("%s:%s\n"%(name[i],data[i]))
    
        