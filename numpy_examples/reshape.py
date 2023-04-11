import numpy as np

a = np.arange(6)
print("an array:",a)

c = a.reshape(2,3)
d = a.reshape(3,2)
f = np.reshape(a, newshape=(2,3), order='C')
print("array with 2 row and 3 column:\n",c)
print("array with 3 row and 2 column:\n",d)
print("array newshape(2,3):\n",f)