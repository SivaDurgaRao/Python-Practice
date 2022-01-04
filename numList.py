#Display numbers from list using loop

l=[]
a=int(input("Enter End number:"))

for i in range(1,a+1):
    val=int(input("Enter value:"))
    l.append(val)
print(l)