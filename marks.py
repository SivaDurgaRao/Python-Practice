
import pandas as pd
std=pd.read_csv("A_Python/Files/Students.csv")

#print(std['marks'].max())
#print(std['marks'].min())
#print(std['marks'].sum())
#print(std['marks'].count())

print(std[std['marks']]>=50)
