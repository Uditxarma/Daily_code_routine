"""Write a Python program to append a new item to the end of the array."""

from array import *
array_num = array('i', [11,22,44,55,66,77,88])
print(array_num)

print("Original array: "+str(array_num))
array_num.append(11)
print(array_num)                #--> print after append