#7. Program to find the position of minimum and maximum elements of a list.

# declare a list of Integers
list = [10, 1, 2, 20, 3, 20]

# min element's position/index
min = list.index (min(list))
# max element's position/index
max = list.index (max(list))

# printing the position/index of min and max elements
print ("position of minimum element: ", min)
print ("position of maximum element: ", max)