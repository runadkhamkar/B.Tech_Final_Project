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
predictor_path = r'shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(predictor_path)
lstpt=[51,57,48,54]
labels=[["begin","choose","connection","navigation","next","previous","start","start","stop","hello","web"],["stop navigation","excuse me","i am sorry","thank you","good bye","i love this game","nice to meet you","you are welcome","how are you","have a goog time"]]
win = dlib.image_window()
img = cv2.imread("G:\\platform-tools\\Miracle\\M01\\phrases\\01\\01\\color_001.jpg",0)
rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
dets = detector(rgb_image,1)
win.clear_overlay()
temp2=[]
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
cv2.destroyAllWindows()
print(temp2)

#%%
for i,d in enumerate(dets):
    print(i,d.left())
