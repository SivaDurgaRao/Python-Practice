#4. Program to find the differences of two lists.

l1 = [10, 15, 20, 25, 30, 35, 40]
l2 = [25, 40, 35]

l3=list(set(l1) - set(l2)) + list(set(l2) - set(l1))
print(l3)

l4= [i for i in l1 + l2 if i not in l1 or i not in l2]
print(l4)