import numpy as np

a=np.arange(10)
print(a)
print("reversed array: ",np.flip(a))


b=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("reversed 2D array:\n",np.flip(b))
print("reversed 2D array:\n",np.flip(b,axis=0))
print("reversed 2D array:\n",np.flip(b,axis=1))