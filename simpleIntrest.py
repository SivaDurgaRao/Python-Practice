'''2. Write a Python program to calculate the Simple Interest by taking the values dynamically from the user. Formula: PNR/100

Input:
Enter the principal amount: Rs.25000 Enter the time(years): 2
Enter the rate: 5
Output:
The simple interest is: R 2500.0'''

P=float(input("Enter Principle Amount:"))
T=int(input("Enter time perid:"))
R=float(input("Rate of interest:"))

SI=(P*T*R)/100

print("The simple Interest is:",SI)