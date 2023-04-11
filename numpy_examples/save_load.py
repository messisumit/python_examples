import numpy as np
# used for save and load numpy object
a=np.array([1,2,3,4,5,6,7,8,9])
np.save('save_load',a)
b=np.load('save_load.npy')
print(b)



# used to save and load data in either csv or txt
a=np.array([1,2,3,4,5,6,7,8,9])
np.savetxt('save_load.csv',a)
b=np.loadtxt('save_load.csv')
print(b)