import pandas as pd
std=pd.read_csv("A Python/Files/Students.csv")

print(std[std['city']=='Pune'])

print(std[std['gender']=='female'])