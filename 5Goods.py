'''5. Write a program that accepts cost of goods sold (cgos) revenue generated, operating costs (oc) and prints Gross profit, net profit and net profit percentage.
Hint: Net profit = Revenue – cgos – oc

Input:
500
3000
300
Output:
Gross profit is 2500 Net profit is 2200
Net profit percentage is 73.33333333333333
'''


cgos = int(input('Enter cost of goods sold : '))
rg = int(input('Enter revenue generated : '))
oc = int(input('Enter operating cost : '))
gp = rg - cgos
np = gp - oc 
npp = np/rg*100 
print('Gross profit is', gp)
print('Net profit is', np)
print('Net profit percentage is', npp)