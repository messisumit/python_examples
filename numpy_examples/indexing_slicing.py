import numpy as np

a=np.array([1,2,3,4,5,6,7,8])
b=a[2],a[2:],a[:4],a[-2:]
print(b)

divisible_by_2=a[a%2==0]
print(divisible_by_2)

c=[(a>2)&(a<10)]
print(c)

d=(a>5)|(a==5)
print(d)

