import numpy as np
from numpy import dtype

data=np.array([2,3])
ones=np.ones(2,dtype=int)
print(data+ones)
print(data-ones)
print(data*ones)
print(data/ones)
print(data.sum())

b=np.array([[1,1],[2,2]])
print(b.sum(axis=0))
print(b.sum(axis=1))

