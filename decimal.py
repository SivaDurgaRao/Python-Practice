n=int(input("Enter num:"))
l=[]
while n:

    r=n%2
    l.append(r)
    n=n//2
for i in range(len(l)-1,-1,-1):
    print(l[i],end=" ")