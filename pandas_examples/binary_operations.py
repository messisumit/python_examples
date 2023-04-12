import pandas as pd

df=pd.Series([3,5,9,80],index=['a','b','c','d'])
df1=pd.Series([2,98,43,21],index=['a','b','e','d'])

print(df,'\n',df1)

a= df.add(df1,fill_value=0)
b=df.sub(df1,fill_value=0)
print("after addition",a)
print("\n after subtracting ",b)