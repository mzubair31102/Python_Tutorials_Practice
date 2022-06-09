#Dictionaries are used to store data values in key:value pairs.
Student_details={
    "id":25,
    "Name":"Zubair",
    "Class":"MS",
    "Hight":3.7,
}
print(Student_details)
print(type(Student_details))
#Dictionary items are ordered, changeable, and does not allow duplicates.
#Changeable
#Duplicates Not Allowed
#Dictionary Length
print(len(Student_details))
#Dictionary Items - Data Types
#Accessing Items
print(Student_details["Name"])
print(Student_details.get("Name"))
#Get Keys
print(Student_details.keys())
#Get Values
print(Student_details.values())
#Get Items
print(Student_details.items())
#Check if Key Exists
if "Name" in Student_details:
    print("Yes Name Key is There")

#Change Values
Student_details["Name"]="Ali"
print(Student_details)
#Update Dictionary
Student_details.update({"Name":"Waqar"})
print(Student_details)
#Adding Items
Student_details["Address"]="Lahore"
print(Student_details)
#Update Dictionary
Student_details.update({"Age":25})
print(Student_details)
#Removing Items
Student_details.pop("Age")
print(Student_details)
del Student_details["Address"]
print(Student_details)
Student_details.popitem()
print(Student_details)
#del Student_details
#print(Student_details)
#Clear method
#Student_details.clear()
#print(Student_details)
#Loop Through a Dictionary
for i in Student_details:
    print(i)
for i in Student_details:
    print(Student_details[i])
#Copy a Dictionary
Student_details_copy = Student_details
Student_details_new_copy=dict(Student_details)
print(id(Student_details))
print(id(Student_details_copy))
print(id(Student_details_new_copy))
#Nested Dictionaries
All_Student_details={
    "std1":{
        "id":25,
        "Name":"Zubair",
        "Class":"MS",
        "Hight":3.7,
    },
    "std2": {
        "id": 25,
        "Name": "Zubair",
        "Class": "MS",
        "Hight": 3.7,
    },
    "std3": {
        "id": 25,
        "Name": "Zubair",
        "Class": "MS",
        "Hight": 3.7,
    }
}
print(All_Student_details)
#Copy
#pop
#pop item
#SetDefault
#Update
#Values

