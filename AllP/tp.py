import sys
import dlib
import cv2
import time
import os,glob
import threading
import math
import matplotlib.pyplot as plt
import numpy as np
from python_speech_features import mfcc
from hmmlearn.hmm import GaussianHMM as Gh

detector = dlib.get_frontal_face_detector()
predictor_path = r'shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(predictor_path)
sw=2
data=[]
str1="bbbl8p.mpg"
print(str1)
cam=cv2.VideoCapture(str1)
count=0
st=time.time()
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
    ft=time.time()
    if cv2.waitKey(1) == 1:
        break
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
    h1.append(int(abs(m*i[1][0]-i[1][1]+c)/math.sqrt(m**2+1)))
    h2.append(int(abs(m*i[5][0]-i[5][1]+c)/math.sqrt(m**2+1)))
    h3.append(int(abs(m*i[2][0]-i[2][1]+c)/math.sqrt(m**2+1)))
    h4.append(int(abs(m*i[4][0]-i[4][1]+c)/math.sqrt(m**2+1)))
d.append(h1)
d.append(h2)
d.append(h3)
d.append(h4)
data.append(d)

m1=Gh(n_components=4,covariance_type="diag",n_iter=1000)
b1=np.array([])
"""
for i in d:
    freq=mfcc(i,8000)
    if(len(b1)==0):
        b1=i
    else:
        b1=np.append(b1,i,axis=0)
print(b1.shape)
print(m1.fit(b1))
"""
print(type(d[0][0]))
freq=np.array([])
for i in d:
    a=mfcc(d[0],800)
    if(len(freq)==0):
        freq=a
    else:
        freq=np.append(freq,a,axis=0)
models=[]
for i in range(0,4):
    m1=Gh(n_components=4,covariance_type="diag",n_iter=1000)
    m1.fit(freq[i])
    models.append(m1)






