#Display fibonacci series upto 10 terms
first=0
second=1
for i in range(1,11):
    print(first)
    temp=first
    first=second
    second=temp+first