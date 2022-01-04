NumList = []
Number = int(input("How many element in list, Please enter num : "))
for i in range(1, Number+1):
    value = int(input("Please enter the Value:"))
    NumList.append(value)
 
smallest = NumList[0]
 
for j in range(1, Number):
    if(smallest > NumList[j]):
        smallest = NumList[j]

 
print("The Smallest Element in this List is : ", smallest)