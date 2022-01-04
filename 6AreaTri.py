'''6. Write a Python program to calculate the Area of a Triangle
Formula:
If a, b and c are three sides of a triangle. Then, s = (a+b+c)/2
area = √(s(s-a)*(s-b)*(s-c))
'''

from math import*

a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
s = (a + b + c) / 2
area = (m.sqrt(s*(s-a)*(s-b)*(s-c)))
print("The area of the triangle is",area)