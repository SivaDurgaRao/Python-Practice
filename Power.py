'''3. Write a Python program to read a number n from the user and compute n+nn+nnn
Example: If the n = 5
5+55+555 = 615

Input:
Enter a number n: 5
Output:
The value is: 615

Input:
Enter a number n: 20
Output:
The value is: 204060'''

'''n=int(input("Enter n value:"))
Output=(n(1+11+111))

print("Output is:",Output)
'''

n=int(input("enter number n:"))
temp=str(n)
t1=temp+temp
t2=temp+temp+temp
comp=n+int(t1)+int(t2)
print(comp)
