'''7. Write a Python program to prints all integers that aren’t divisible by
either 2 or 3 and lies between 1 and 50

Output Format:
Line 1: <numbers separated by space>

Output:
1 5 7 11 13 17 19 23 25 29 31 35 37 41 43 47 49
'''

for i in range(0,51):
    if(i%2!=0 and i%3!=0):
        print(i,end=" ")