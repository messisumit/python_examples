import numpy as np
import pandas as pd
series=pd.Series()
print(series)
data = np.array(['hello','!','how','are','you'])
series=pd.Series(data)
print(series)
# accessing specific elements of data
print(series[:2])



# accessing single element using index label
data = np.array(["s","u",'m','i','t','k','u','m','a','r','v','a','j','p','a','y','e','e'])
ser=pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27])
print("accessing element of through index:",ser[19])