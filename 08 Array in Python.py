# Array in Python
from array import *

# Syntax arrayName = array(typecode, [Initializers])
array_num = array("i",[1,3,5,7,8,9])
print(type(array_num))
print(type(array_num[1]))
"""
Typecode 	 Value
   b 	      Represents signed integer of size 1 byte/td>
   B 	      Represents unsigned integer of size 1 byte
   c 	      Represents character of size 1 byte
   i 	      Represents signed integer of size 2 bytes
   I 	      Represents unsigned integer of size 2 bytes
   f 	      Represents floating point of size 4 bytes
   d 	      Represents floating point of size 8 bytes"""
# Basic Operations
# Traverse − print all the array elements one by one.
arr_num = array("i",[1,3,5,7,8,9])
for i in arr_num:
    print(i)
# Insertion − Adds an element at the given index.
print("Insertion")
arr_num.insert(2,6)
for i in arr_num:
    print(i)
# Deletion − Deletes an element at the given index.
print("Deletion")
arr_num.remove(7)
for i in arr_num:
    print(i)
# Search − Searches an element using the given index or by the value.
arr_num1 = array("i",[1,3,5,7,8,9])
print(arr_num1.index(5))
print(arr_num1[4])
# Update − Updates an element at the given index.
arr_num1[2]=15
for i in arr_num1:
    print(i)