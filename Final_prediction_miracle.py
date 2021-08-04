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
#%%
cam=cv2.VideoCapture("G:\platform-tools\\test1.mp4")
st=time.time()
temp=[]
count=0
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
    count+=1
    for k, d in enumerate(dets):
        shape = predictor(img, d)
        A=d.left()
        B=d.top()
        C=d.right()
        D=d.bottom()
        d1=C-A
        d2=D-B
        Area=d1*d2
        for i in lstpt:
            temp1=[]
            temp1.append(shape.part(i).x)
            temp1.append(shape.part(i).y)
            temp2.append(temp1)
            win.add_overlay(shape)
        a=math.sqrt((temp2[0][0]-temp2[1][0])**2+(temp2[0][1]-temp2[1][1])**2)
        b=math.sqrt((temp2[2][0]-temp2[3][0])**2+(temp2[2][1]-temp2[3][1])**2)
        temp.append(a*b*0.5/Area)
    win.add_overlay(dets)
    #temp.append(temp2)
    if cv2.waitKey(1) == 1:
        break
cv2.destroyAllWindows()

#%%
len(temp)
l=[]
b=0
for i in temp:
    if(b==0):
        l.append(i)
        b+=1
    else:
        b-=1
l=l[:11]
model=pickle.load(open("G:\platform-tools\\MiracleB.pickle","rb"))
print(model.predict([l]),model.predict_proba([l]))


