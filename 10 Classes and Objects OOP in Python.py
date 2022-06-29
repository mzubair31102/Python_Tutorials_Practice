# A Class is like an object constructor,
# or a "blueprint" for creating objects.
# Python Classes/Objects
# Create a Class
class Customer:
    print("I am a Class")
# Create an Object
cum1_obj= Customer
# The __init__() Function
class Student:
    def __init__(self, id, Name, Email):
        self.Name=Name
        self.id =id
        self.Email = Email
        print("Values Auto Assigned")
    def std_details(self):
        print(self.id,self.Name,self.Email)
obj1=Student(23,"M.Zubair","abc@gmail.com")
obj2=Student(12,"Ali","xyz@gmail.com")
obj1.std_details()
obj2.std_details()
name="Koi name Nahi"
# Object Methods
class Customer1:
    def __init__(self, email,name ):
        self.email = email
        self.name = name
    def buy_product(self,cont):
        print(self.name)
        return cont*500
cum1 = Customer1("abc@gmail.com","Waqar")
print(cum1.buy_product(23))
# The self Parameter
# Modify Object Properties
cum1.name = "Waseem"
print(cum1.name)
# Delete Object Properties
del cum1.name
print(cum1.name)
# Delete Objects
del cum1
