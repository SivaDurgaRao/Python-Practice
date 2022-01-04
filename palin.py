a=151
temp=a
b=len(str(a))
sum=0
for i in range(0,b):
    v=a%10
    sum=sum*10+v
    
    a=a//10
print(sum)
if sum==temp:
    print("palindrome")
else:
    print("not")