import numpy as np

array_example = np.array([[[0, 1, 2, 3],[4, 5, 6, 7]],

                          [[0, 1, 2, 3],[4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],[4, 5, 6, 7]]])
a=array_example.ndim
b=array_example.size
c=array_example.shape

print("dimension:",a,"\nno.of elements:",b,"\nshape of array:",c)