import numpy as np
import pandas as pd

dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
df=pd.DataFrame(dict)


# boolean value of dict by isnull() function
# bolean value of dict by notnull() function
x=df.isnull()
y=df.notnull()
print("bolean value of null",x)
print("\nboolean value of not null",y)


# filling nan values by 0 using fillna() function
z=df.fillna(0)
print("\nfilling empty value with 0",z)

# dropping values of nan by dropna() function
a=df.dropna()
print("\ndropping NAN values",a)