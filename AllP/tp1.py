import numpy as np
from hmmlearn.hmm import GaussianHMM as Gh
import random as rd


x=np.array([[rd.randint(-10,10) for i in range(0,3)]for j in range(0,5)])
X=np.column_stack([x])
print(X)
print(X.shape)
model=Gh(n_components=2,covariance_type="diag",n_iter=1000)
print(model.fit(X))

a,b=model.sample(10)
for i in range(0,len(a)):
	print(a[i],":",b[i])