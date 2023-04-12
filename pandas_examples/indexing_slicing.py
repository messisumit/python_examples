import pandas as pd

data=pd.read_csv("nba.csv")
ser=pd.Series(data['Name'])
x=ser.head(23)
print(x)

# specific content using index
y=x[3:6]
print(y)

# using loc
z=x.loc[3:9]
print(z)

# using iloc
a=x.iloc[3:9]
print(a)

