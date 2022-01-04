#1.  Program for Adding, removing elements in the list.

list1=list((20,30,12,45,67,90,34,56))

print ("List elements are: ", list1)


list1[5]="lalitha"
print(list1);
list1[3:6]="apple","mango","Orange"
print(list1)
list1.insert(1,"banana")
print(list1)
list1.append("grapes")
print(list1)

list1.pop () 
print(list1)
list1.remove(12)
print(list1)