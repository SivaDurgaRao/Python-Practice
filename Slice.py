import pandas as pd
std=pd.read_csv("A Python/Files/Students.csv")
#print(std.head(4))
#print(std[:5])
#print(std[1:3])
#print(std[2:3])
#print(std[-5:-3])
#print(std[: :-1])
#print(std[-1:])
#print(std[-2:-5:-1])

data=std.head(5)
print(data)
data.to_csv("A Python/Files/Updated1.csv")