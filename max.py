NumList = []
Number = int(input("How many element in list, Please enter num : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)
 
largest = NumList[0]
 
for j in range(1, Number):
    
    if(largest < NumList[j]):
        largest = NumList[j]

 
print("The Largest Element in this List is : ", largest)
