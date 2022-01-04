'''4. Our task is to help Ross lean the tables.
Let us take the table value to be 2 and the ending count value ro be 10
First print the 2 table. After printing, ask the user whether he wants to continue, if yes then print the next table and so on until the user says no.
Sample Input:
table = 2
 
end = 10
Expected Output:
2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
2 X 4 = 8
2 X 5 = 10
2 X 6 = 12
2 X 7 = 14
2 X 8 = 16
2 X 9 = 18
2 X 10 = 20
Do you want to continue printing the table, press 1 or 0 to Exit: 1 3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
3 X 10 = 30
Do you want to continue printing the table, press 1 or 0 to Exit: 0
'''
n=1
i=1
while(n==1):
    num=int(input("enter Multiplication number "))
    i=1
    while(i<=10):
        print(num,"*",i,"=",num*i)
        i=i+1
    n=int(input("Do you want to continue"))
  
    n=1
i=1
while(n==1):
    num=int(input("enter Multiplication number "))
    i=1
    while(i<=10):
        print(num,"*",i,"=",num*i)
        i=i+1
    n=int(input("Do you want to continue"))
  

    