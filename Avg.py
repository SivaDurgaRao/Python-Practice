'''1. Write Java Python  Program to read 5 marks subject from user and print the Average.
Enter the 1st Subject Mark: 98 Enter the 1st Subject Mark: 87 Enter the 1st Subject Mark: 80 Enter the 1st Subject Mark: 91 Enter the 1st Subject Mark: 94 Output:
Student Information
Marks Secured - 98 , 87 , 80 , 91 , 94
Total = 450
Average Percentage is: 90
'''

print("Enter the marks of five subjects::")

sub1 = int(input ("sub1:"))
sub2 = int(input ("sub2:"))
sub3 = int(input ("sub3:"))
sub4 = int(input ("sub4:"))
sub5 = int(input ("sub5:"))
total = sub1 + sub2 + sub3 + sub4 + sub5
average = (total / 5)

print ("\nThe Total marks is:   \t", total)
print ("\nThe Average marks is: \t", average)