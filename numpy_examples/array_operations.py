import numpy as np

a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])
# basic function
print(a.max())
print(a.sum())
print(a.min())
print(a.min(axis=0))
print(a.min(axis=1))
print(a.max(axis=0))
print(a.max(axis=1))


data=np.array([[1,3],[4,5],[3,9]])
print(data)
print(data.max(axis=0))
print(data.max(axis=1))

# adding matrices
m=np.array([[1,2],[3,4],[6,5]])
ones=np.array([[1,1]])
print(m+ones)

# creating array of ones
print(np.ones((4,3,3)))


#  simplest way to generate random numbers

i=np.random.default_rng()
print(i.random(3))
print(i.random((3,2)))

# generating random numbers
r=np.random.default_rng()
print(r.integers(5,size=(2,4)))

# finding unique elements
z=np.array([11,11,12,13,14,15,16,17,12,14,13,11,16,19])
print(np.unique(z))
print(np.unique(z,return_index=True))

# finding unique element from 2D array
array_2d=np.array([[1,2,3,4],[1,2,3,4],[5,6,7,8],[5,6,7,8]])
print(np.unique(array_2d))
print("unique element ",np.unique(array_2d,axis=0))
print("Occurence count",np.unique(array_2d,axis=0,return_counts=True,return_index=True))