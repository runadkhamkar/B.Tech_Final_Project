








def main():
	A=input("A:")
	B=input("B:")
	c=int(input("C:"))
	a=len(A)
	b=len(B)
	f=open("test1.txt","w")
	X='x'
	Y='y'
	g=''
	while(True):
		temp=X
		X=Y
		Y=temp+Y
		s=0
		d=0
		d1=0
		for i in Y:
			d1=d
			d=s
			if(i=='x'):
				s+=a
			else:
				s+=b
		if(s>c):
			break
	s1=0
	for i in Y:
		if(s1==d1):
			break
		if(i=='x'):
			s1+=a
			Y=Y[1:]
		else:
			s1+=b
			Y=Y[1:]
		print(Y)
	if(Y[0]=='x'):
		g=A
	else:
		g=B
	for i in g:
		d1+=1
		if(d1==c):
			print(i)






if __name__=="__main__":
	main()