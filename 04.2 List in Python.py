
#Lists are used to store multiple items in a single variable.
student_list=["Ali","Zubair","Zubair","Waseem","Adil","Rehman"]
print(student_list)
print(type(student_list))
#List items are ordered (order will not change),
# changeable, and allow duplicate values.
student_list[1]="Uzair"
print(student_list)
#List items are indexed, the first item has index [0]
print(id(student_list[0]))
print(id(student_list[1]))
print(id(student_list[2]))
"""Start List"""
#List Items Data Types
students_id=[1,3,6,8,4]
students_hight=[6.5,7.8,4.5]
students_detail=[21,"Ali",5.9]
print(students_detail)
#list Constructor
list_cst=list((21,"Ali",5.9))
print(list_cst)
print(type(list_cst))
#Access Items
print(student_list[3])
#Negative Indexing
print(student_list[-4])
#Range of Indexes
print(student_list[:3])
#Membership Operator
if "Waqar" not in student_list:
    print("Waqar is not there")
#Change Item Value
student_list[3]="Uzair"
print(student_list)
#Length of List
print(len(student_list))
#Change a Range of Item Values
std_list=["Ali","Zubair","Waseem","Adil","Rehman"]

#Insert Items
std_list.insert(1,"Umair")
print(std_list)
#Append Items
std_list.append("Majeed")
std_list.append("Rashid")
print(std_list)
#Extend List
std_list2=["Iqra","amna","Maryam","Kaneez"]
std_list.extend(std_list2)
print(std_list)
#Remove Specified Item
std_list.remove("Ali")
print(std_list)
print(len(std_list))
#Remove Specified Index
std_list.pop(3)
print(std_list)
print(len(std_list))
#Delete the list completely
#del std_list2
print(std_list2)
#Clear the List
std_list2.clear()
print(std_list2)
#Sort List Alphanumerically
std_list.sort()
print(std_list)
#Sort List Descending
std_list.sort(reverse=True)
print(std_list)
#Case Insensitive Sort
std_list.sort(key=str.lower)
print(std_list)

#Reverse Order
std_list3=["Iqra","amna","Maryam","Kaneez"]
print(std_list3)
std_list3.reverse()
print(std_list3)
#Copy a List
#std_list4=std_list3.copy()
std_list4=list(std_list3)
print(std_list4)
print(id(std_list3))
print(id(std_list4))

#Join Two Lists
std_list5=std_list3+std_list4
print(std_list5)
#For Loop
for x in std_list4:
    print(x)
#Join Two Lists by using Append method
#Join Two Lists by using extend method
#Count List
#Index Method
print(std_list4[2])