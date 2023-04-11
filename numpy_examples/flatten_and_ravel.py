import numpy as np

# flatten change the array into 1d
# flatten does not change the original array
x=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
a1=x.flatten()
a1[0]=99
print("new array after using flatten function:",a1)   # new array changes
print("original array after using flatten function:\n",x)    # original array


# ravel changes the array into 1 d array
# ravel shows the effect on parent array
x=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
a1=x.ravel()
a1[0]=99
print("new array after using ravel function:", a1)   # new array changes
print("original array after using ravel function:\n",x)    # original array
