import numpy as np

a=np.array([1,2,3,4,5,6,7,8,9,10])
arr1=a[2:9]
print(arr1)

a1=np.array([[1,1],
             [2,2]])
a2=np.array([[3,3],
             [4,4]])
b=np.vstack((a1,a2))
print(b)

c=np.hstack((a1,a2))
print(c)

x=np.arange(1,25).reshape(2,12)
y=np.hsplit(x,3)
print(x)
print(y)

e=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
e1=e[0, :]
print(e1)
e1[1]=99
print(e1)

print(e)

f=(e.copy())
print(f)