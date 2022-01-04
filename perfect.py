# Program to find Perfect Number using Functions
 
def Perfect_Number(Number):
    Sum = 0
    for i in range(1, Number):
        if(Number % i == 0):
            Sum = Sum + i
    return Sum        
 

n=int(input("Please Enter any number: "))
if (n==Perfect_Number(n)):
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")