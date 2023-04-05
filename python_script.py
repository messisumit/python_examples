import pandas as pd

file1 = pd.read_csv("expectedIssues1.csv")

for col in range(len(file1)):
    pathway=file1['File'][col]
    print(pathway)
    with open(pathway,"r") as file:
        line=file.readlines()
        print(line)
        line.insert(file1['Line'][col] - 4 , "// Start : Expecting "+file1['CWE'][col]+'\n')
        line.insert(file1['Line'][col] + 4, "\n // End : " + file1['CWE'][col]+'\n')
        with open(pathway,'w') as file:
            line="".join(line)
            file.write(line)






