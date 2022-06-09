# Store multiple items in a single variable
# Unchangeable(but we can remove items and add new items)
# Unordered (cannot be referred to by index)
# Do not allow duplicate values
# Example
Students={"ali","umer","zubair","umair","waqar","ahmed"}
print(Students)
print(type(Students))
# By the Constructor
#Students_c=set(("ali","umer","zubair","zubair","umair","waqar","ahmed"))
#print(type(Students_c))
# Length of a Set
print(len(Students))
# Set Items Data Types
student_details={25,"Umair",5.2}
print(student_details)
print(type(student_details))
# Access Items (cannot access items in a set by index)
for i in Students:
    print(i)
# Add Items (by add function)
Students.add("Hassan")
print(Students)
# Add Sets (by update function)
Students_girls={"Nimra","Alina","Aqsa"}
#Students.update(Students_girls)
# Add Any Iterable
# Remove Item....
#Students.remove("Rashid")
#print(Students)
Students.discard("Rashid")
print(Students)
Students_girl={"Nimra","Alina","Aqsa"}
Students_girls.pop()
print(Students_girls)
#Students_girls.clear()
#print(Students_girls)
#del Students_girls
print(Students_girls)
# Loop Items
for i in Students:
    print(i)
# Join Two Sets
set1={"Apple","Orange","Banana","Banana"}
set2={"Ali","Orange","Waqar"}
set3=set2.union(set1)
print(set3)
# Keep ONLY the Duplicates
"""set1.intersection_update(set2)
print(set1)
set_inter=set1.intersection(set2)
print(set_inter)"""
# Keep All, without Duplicates
set3={"Apple","Orange","Banana","Banana"}
set4={"Ali","Orange","Waqar"}
#set3.symmetric_difference_update(set4)
set5=set4.symmetric_difference(set3)
print(set5)
# Copy Method
set7=set4.copy()
print(set4)
print(set7)
# Difference Method
set_a={"Apple","Orange","Banana"}
set_b={"Ali","Orange","Waqar"}
set_c=set_b.difference(set_a)
print(set_c)