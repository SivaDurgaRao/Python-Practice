import pandas as pd
std=pd.read_csv("A Python/Files/Students2.tsv", sep="\t")
#print(std.head(4))
#print(std.tail(3))

print(std)

std.to_csv("A Python/Files/Students.csv")