'''3. Ron has been given 10 numbers which includes both positive and negative values by his teacher. His task is to tell the total of positive and negative numbers separately. Our task is to help him in this task. 

Sample Input:
10
50
-30
15
-45
-96
5
78
-99
253

Expected Output:
Sum of Positive Numbers = 411 Sum of Negative Numbers =-270
'''

NumList = []
Positive = []
Negative = []

Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] >= 0):
        Positive.append(NumList[j])
    else:
        Negative.append(NumList[j])

print("Element in Positive List is : ", Positive)
print("Element in Negative List is : ", Negative)
