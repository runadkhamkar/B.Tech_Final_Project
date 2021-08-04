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
win = dlib.image_window()
img = cv2.imread("G:\\platform-tools\\Miracle\\F01\\phrases\\01\\01\\color_001.jpg",0)
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
temp.append(temp2)
ft=time.time()
if cv2.waitKey(1) == 1:
    break
cv2.destroyAllWindows()
