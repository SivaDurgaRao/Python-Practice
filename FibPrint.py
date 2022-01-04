'''5. Write a Python program to check whether the given number is a Fibonacci Number or not.

Input Format:
Line 1: <Integer Number>
Output Format:
Line 1: <1 -> if the number is a Prime Number>
<0 -> if the number is not a Prime Number>

Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 141, .. (Fibonacci series is the sum of the previous two terms)

Input:
8
Output:
1
'''
n=int(input("Enter num:"))
a = 0
b = 1
print(a)
print(b)
for i in range(2,n):
    c = a + b
    a = b
    b = c
    print(c,end=" ")