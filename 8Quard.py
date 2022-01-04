'''8: Write a Python program to solve the Quadratic Equation
Formula:
ax2 + bx + c = 0, where
a, b and c are real numbers and
a ≠ 0'''


from math import*
a=int(input("enter number a:"))
b=int(input("enter number b:"))
c=int(input("enter number c:"))

d = (b**2) - (4*a*c)

s = (-b-(sqrt(d)))/(2*a)

print(('The solution is').format(s))