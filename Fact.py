#Factorial of a number
n=int(input("Enter num for factorial:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of",n,"is:",fact)