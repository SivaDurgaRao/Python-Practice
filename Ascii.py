'''5.: Write a Python program to print the ASCII Character for the given
integer value
Input:
Enter a Number: 35
Output:
ASCII equivalent of 35 is #
Input:
Enter a Number: 125
Output:
ASCII equivalent of 125 is }
Input:
Enter a Number: 50
Output:
ASCII equivalent of 50 is 2'''
for i in range(0,num):
    num=int(input("enter number"))
    print("ASCII equivalent of ",num,"is",ord(num))