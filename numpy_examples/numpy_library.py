# numpy library
import numpy as np
# concatenate and sorting two array
a=np.array([1,2,3,4,5,6,8])
b=np.array([2,3,4,5,1,2,3,4])
c=np.concatenate((a,b))
arr=np.sort(c)
print(c)
print(arr)

# indexing of array
d=np.array([[1,2,3],[2,3,4],[3,4,2]])
e=np.array([[9,8,7],[8,7,6]])
f=np.concatenate((d,e),axis=0)
arr1=np.sort(f)
print(f)
print(arr1)
