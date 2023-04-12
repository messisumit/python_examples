import numpy as np
import pandas as pd
series=pd.DataFrame()
print(series)
lst = ['hello','!','how','are','you']
series=pd.DataFrame(lst)
print(series)

# after initializing data in list
data={'Name':['amit','sumit','archana','anil','sunita'],
      'age':[24,23,27,49,49],
      'address':['chandigarh','pune','raipur khurd','chandi','chand'],
      'qualification':['mcom','btech','bcom','ba','housewife']}
series=pd.DataFrame(data)
print(series[['Name','qualification']])