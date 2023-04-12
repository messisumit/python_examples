import pandas as pd
data = pd.read_csv("nba.csv",index_col="Name")
x=data.iloc[7]
y=data.iloc[9]
print(x,y)