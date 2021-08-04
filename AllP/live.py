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
sw=2
data=[]
path="G:\\platform-tools\\s1\\"
#path="G:\\platform-tools\\bbil1n.mpg"
inpt=input("Enter the video name:")
str1=path+"\\"+inpt+".mpg"
cam=cv2.VideoCapture(str1)
count=0
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
        count+=1
        for i in lstpt:
            temp1=[]
            temp1.append(shape.part(i).x)
            temp1.append(shape.part(i).y)
            temp2.append(temp1)
            win.add_overlay(shape)
    win.add_overlay(dets)
    temp.append(temp2)
    #temp.append(temp2)
    ft=time.time()
    if cv2.waitKey(1) == 1:
        break
cv2.destroyAllWindows()
d=[]
for i in temp:
    a=math.sqrt((i[0][0]-i[1][0])**2+(i[0][1]-i[1][1])**2)
    d.append(round(a,2))
#%%

#%%
classifier=pickle.load(open("G:\\platform-tools\\s1.pickle","rb"))
print("classified text:",classifier.predict(d))
#%%