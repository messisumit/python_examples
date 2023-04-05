# importing csv to read csv file
import csv
import os

# open file using with so that it automatically close the file after operation,
with open('expectedIssues1.csv', 'r') as f:
    # I use the csv.DictReader class to read the CSV file as a dictionary.
    # This allows us to access the values in each row using their column names:
    reader = csv.DictReader(f)
    # iterating each row
    for row in reader:
        # storing file path in path
        path = row['File']
        with open(path, "r") as file:
            # reading and inserting two comments in file
            lines = file.readlines()
            lines.insert(int(row['Line']) - 4, "// Start: Expecting " + row['CWE'] + "\n")
            lines.insert(int(row['Line']) + 4, "// End: " + row['CWE']+"\n")
        with open(path, 'w') as file:
            # writing modified lines back to the original file
            file.write("\n".join(lines))
