import pandas as pd
std=pd.read_csv("Pandas/Files/Students.csv")

data=std.head(5)

print(data)

data.to_csv("A Python/Files/updatedfile.csv",index=False)