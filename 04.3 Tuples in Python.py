#store multiple items in a single variable.
firsttuple=("ali","ali","waqar","umar","waseem","majid")
print(firsttuple)
print(type(firsttuple))
# Tuple by using Constructor
tuple_by_c=tuple(("ali","ali","waqar","umar","waseem","majid"))
print(tuple_by_c)
print(type(tuple_by_c))
#ordered, unchangeable (not allow to add delete or repalce), and allow duplicate values..
#firsttuple[1]="Zubair"
#print(firsttuple)
#tuples are indexed, they can have items with the same value:
#TUPLE examople
Students=("ali","ali","waqar","umar","waseem","majid")
Students_girls=("Asima","Amina","Aqsa")
#Tuple Length
print(len(Students))
#Tuple With One Item
student=("zubair",)
print(type(student))
#Tuple Items Data Types
student_details=(23,"Ali",2.9)
print(student_details)
print(type(student_details[0]))
#Access Tuple Items
print(Students[3])
#Range of Indexes
print(Students[:5])
# Nagitive indexing
print(Students[-2:])
# Membership operators
if "zahid" not in Students:
    print("Yes ali is there")
#Tuple into a list then change the value and then again convert to tuple &Add Items (by converting into list)
Students_list=list(Students)
print(type(Students_list))
print(Students_list)
Students_list[1]="Ahmed"
Students_list.append("Hassan")
print(Students_list)
Students=tuple(Students_list)
print(Students)
print(type(Students))
#Add tuple to a tuple.
all_students=Students+Students_girls
print(all_students)
#Remove Items
remove_student_details=(23,"Ali",2.9)
list_student_details=list(remove_student_details)
list_student_details.remove("Ali")
print(list_student_details)
remove_student_details=tuple(list_student_details)
print(remove_student_details)
#Delete the tuple completely
del remove_student_details
#print(remove_student_details)

#Unpacking a tuple
std_details=(23,"Ali",2.9)
(id,name,hight)=std_details
print(id)
print(type(id))
print(name)
print(type(name))
print(hight)
print(type(hight))
#Using Asterisk*
(*remaning,hight)=std_details
print(remaning)
print(hight)
#Loop Through a Tuple.
for y in Students:
    print(y)
#Loop Through the Index Numbers
for i in range(len(Students)):
    print(Students[i])
#count Method
std_d=(23,"Ali","Ali","Ali","Ali",2.9)

print(std_d.count("Ali"))
