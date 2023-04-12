import pandas as pd

dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
x=pd.DataFrame(dict)
for i,j in x.iterrows():
    print(i,j)

column=list(x)
for i in column:
    print(x[i][3])
