import pandas as pd

data=pd.read_csv("nba.csv")
data.dropna(inplace=True)
before=data.dtypes
data['Salary']=data['Salary'].astype(int)
data['Number']=data['Number'].astype(str)
after=data.dtypes

print("before conversion:",before)
print("after conversion:",after)