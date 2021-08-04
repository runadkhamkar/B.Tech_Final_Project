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
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

def t1(str1):
	cam=cv2.VideoCapture(str1)
	count=0
	temp=[]
	lstpt=[51,57,48,54]
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
	d1=[]
	d2=[]
	if(len(temp)==0):
		return str1,1
	for i in temp:
		a=math.sqrt((i[0][0]-i[1][0])**2+(i[0][1]-i[1][1])**2)
		b=math.sqrt((i[2][0]-i[3][0])**2+(i[2][1]-i[3][1])**2)
		d1.append(round(a,2))
		d2.append(round(b,2))
	d=[]
	d.append(d1)
	d.append(d2)
	return str1,d
#%%
name=[]
def f1():
	path="s5"
	lstdir=os.listdir(path)
	print(lstdir)
	start=time.time()
	data=[]
	dir1=[]
	for f in glob.glob(path+"\\s5\\*.mpg"):
	    dir1.append(f)
	st=time.time()
	with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
	    g = {executor.submit(t1, dir1[i]): dir1[i] for i in range(0,len(dir1))}
	for i in concurrent.futures.as_completed(g):
	    a,b=i.result()
	    data.append(a)
	    data.append(b)
	ft=time.time()
	print(ft-st)
	with open(path+"/s5.txt","wb") as file:
	    pickle.dump(data,file)
print("Total time:",time.time()-start)

#%%
if __name__=="__main__":
    f1()

    
        
