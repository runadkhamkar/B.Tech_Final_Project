from hmmlearn.hmm import GaussianHMM as Gh
from hmmlearn import hmm
import numpy as np
import random as rd
model=hmm.MultinomialHMM(n_components=5,n_iter=100)
x=[[((-1)**(j+i))*(i+j) for i in range(0,5)]for j in range(0,5)]
print(x)
#len1=len(x)

x=np.array(x)
model.fit(x)
print(model.predict(x))
a,b=model.sample(10)
for i in range(0,len(a)):
	print(a[i],"=",b[i])
t=[[(-1)**(i+j)*rd.randint(-10,10) for i in range(0,4)]for j in range(0,4)]
print(t)
print(model.predict(np.array(t)))
print(model.predict_proba(t))

