#Display Reverse integer
'''
n=input("Enter number:")
for i in n:
    pass

print("Reversed number:",n[::-1])
'''
    
n=int(input("Enter number:"))
rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    r=n//10
print(r,end="")
    