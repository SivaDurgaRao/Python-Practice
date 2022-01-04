#6. Python program to multiply all numbers of a list.

myList = []
length = int(input("Enter number of elements: "))
for i in range(0, length):
    value = int(input())
    myList.append(value)

# multiplying all numbers of a list
productVal = 1
for i in myList:
    productVal=productVal*i

# Printing values 
print("List : ", myList)
print("Product of all values = ", productVal)