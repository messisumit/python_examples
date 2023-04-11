import numpy as np


# TRANSPOSING AND RESHAPING ARRAY

data=np.arange(6)
x=(data.reshape(2,3))
print(data.reshape(2,3))
y=data.reshape(3,2)
print(x.transpose())
print(y.transpose())
print(y.T)