#Display a list of elements in odd index position 
l=[1,2,3,4,5,6,7,8,9]
a=len(l)
for i in range(a):
    if i%2!=0:
        print(l[i])