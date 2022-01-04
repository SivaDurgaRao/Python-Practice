num = int(input("Enter a number \n"))
sumOfFactors = 0

#Calculating the sum of Factors
for i in range(1,num):
    if num%i == 0:
        sumOfFactors += i;

if sumOfFactors == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")