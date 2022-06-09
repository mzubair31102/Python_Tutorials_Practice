# Boolean Data Type in Python
# When we compare two values, the expression is evaluated
# and Python returns the Boolean answer True or False.
# Expression
print(3<4)
# Conditions
a=10
b=4
if a<b:
    print("Yes B is Greater")
else:
    print(" B is not Greater then A")
# bool function
print(bool(""))
print(bool("ALi"))
print(bool(0))
print(bool(5))
print(bool(None))
print(bool(["ali","umar","waqar"]))
print(bool([]))
# Functions can Return a Boolean
def myfunction():
    return False
print("Print Function's Result")
print(myfunction())
# Check object is of a certain data type
var="4"
print(isinstance(var,str))