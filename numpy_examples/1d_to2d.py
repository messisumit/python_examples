import numpy as np

a=np.arange(4)
b=a[np.newaxis, :]
print(b.shape)

row_vector= a[np.newaxis,:]
print(row_vector.shape)

col_vector=a[:,np.newaxis]
print(col_vector.shape)


b = np.expand_dims(a, axis=1)
print(b.shape)

c = np.expand_dims(a, axis=0)
print(c.shape)