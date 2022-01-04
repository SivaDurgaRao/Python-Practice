s={1,2,3,12,4,5,6}
temp=0
for i in s:
    for j in s:
        if i<j:
            temp=j
            j=i
            i=temp
print(i)