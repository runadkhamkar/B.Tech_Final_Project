from hmmlearn import hmm
import numpy as np
model=hmm.GaussianHMM(n_components=3,covariance_type="full")
model.startprob_=np.array([0.5,0.1,0.4])
model.transmat_=np.array([[0.9,0.0,0.1],[0.2,0.8,0.0],[0.0,0.1,0.9]])
model.means_=np.array([[0.0,0.1],[0.1,0.5],[0.5,0.8]])
model.covars_=np.tile(np.identity(2),(3,1,1,))
a,b=model.sample(100)
print(b)
model1=hmm.GaussianHMM(n_components=3,covariance_type="full")
x=np.array([[0.9,0.0,0.1],[0.0,0.2,0.8],[0.0,0.1,0.9]])
model1.fit(x)
print(model1)
#print(model1.predict_proba(x))
a,b=model1.sample(100)
print(b)
"""
x=np.array([[0.5 for i in range(0,5)]])
model2=hmm.GaussianHMM(n_components=5)
print(model2.fit(x,5))
"""