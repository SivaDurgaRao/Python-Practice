'''6. Write a Python program to check whether the given number is a Palindrome or not.
Palindrome -> the number is equal to the reverse of the number

Input Format:
Line 1: <Integer Number>
Output Format:
Line 1: <1 -> if the number is a Palindrome Number>
<0 -> if the number is not a Palindrome Number>

Input:
123
Output:
0

Input:
1111
Output:
1

Input:
1
Output:
1

Input:
121
Output:
 
1
'''
rev=0
n=int(input("enter n value:"))
temp=n;
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if temp==rev:
    print("1")
else:
    print("0")
