#%%
import sys
import dlib
import cv2
import time
import os,glob
import threading

import math
import matplotlib.pyplot as plt


#%%
detector = dlib.get_frontal_face_detector()
predictor_path = r'G:\\platform-tools\\shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(predictor_path)
sw=2
data=[]
#str1=raw_input("Enter the video name:")
#print(str1)
cam=cv2.VideoCapture("G:\\platform-tools\\bbaf1n.mpg")
count=0
st=time.time()
temp=[]
lstpt=[51,57,48,54]
#win = dlib.image_window()
while True:
    ret_val, img = cam.read()
    if(ret_val==False):
        break
    rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dets = detector(rgb_image,1)
    temp2=[]
    #win.clear_overlay()
    #win.set_image(img)
    for k, d in enumerate(dets):
        shape = predictor(img, d)
        count+=1
        for i in lstpt:
            temp1=[]
            temp1.append(shape.part(i).x)
            temp1.append(shape.part(i).y)
            temp2.append(temp1)
            #win.add_overlay(shape)
    #win.add_overlay(dets)
    temp.append(temp2)
    temp.append(temp2)
    ft=time.time()
    if cv2.waitKey(1) == 1:
        break
    if(ft-st>=5):
        break
#cv2.destroyAllWindows()
#%%
d=0
d1=0
h1=[]
h2=[]
h3=[]
h4=[]
for i in temp:
    if(len(i)==0):
        break
    d=math.sqrt((i[0][0]-i[1][0])**2+(i[0][1]-i[1][0])**2)
    d1=math.sqrt((i[2][0]-i[3][0])**2+(i[2][1]-i[3][0])**2)
    h1.append(d*d1*0.5)

#%%
print("Time:",time.time()-st)
