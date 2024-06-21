"""Write a Python program to create an array of 5 integers and display the array items. 
    Access individual elements through indexes."""

'''Note:Python does not have built-in support for Arrays, but Python Lists can be used instead.'''

from array import *
array_num = array('i', [111,222,333])
# print(len(a))         #len()-The length of an array is always one more than the highest array index.

for i in array_num:
    print(i, end =" ")

print("\nAccess first three items individually:")
#print list elements by index
print(array_num[0])
print(array_num[1])
print(array_num[2])

