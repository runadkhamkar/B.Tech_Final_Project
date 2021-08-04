from multiprocessing import Process
import time
import threading
import concurrent.futures
import os


def function1(z):
	print("Multiprocessing")
	st=time.time()
	print("f1:",st)
	p=Process(target=t1,args=(z,))
	p1=Process(target=t1,args=(z,))
	p2=Process(target=t1,args=(z,))
	p3=Process(target=t1,args=(z,))

	p.start()
	p1.start()
	p2.start()
	p3.start()

	p.join()
	p1.join()
	p2.join()
	p3.join()
	ft=time.time()
	print("F1:",(ft-st))

def t1(n):
	print("Pid:",os.getpid())
	s=1
	while(n>=1):
		s*=n
		n-=1
	print(s)

def function2(n):
	print("Threading")
	st=time.time()
	print("f2:",st)
	x=[]
	for i in range(0,4):
		t=threading.Thread(target=t1,args=(n,))
		x.append(t)
	for i in range(0,4):
		x[i].start()
	for i in range(0,4):
		x[i].join()
	ft=time.time()
	print("F2:",(ft-st))

def function3(n):
	print("Simple for loop")
	st=time.time()
	print("f3:",st)
	for i in range(0,4):
		t1(n)
	ft=time.time()
	print("F4:",(ft-st))


def function4(n):
	print("Concurrent futures")
	st=time.time()
	print("f4:",st)
	x=[n for i in range(0,10)]
	with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
		d={pool.submit(t1,n):n for i in range(0,4)}
	ft=time.time()
	print("F4:",(ft-st))
	

if __name__=="__main__":
	n=int(input("E:"))
	#print("sdjhf")
	function4(n)
	function3(n)
	function2(n)
	function1(n)
