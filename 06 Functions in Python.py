#A function is a block of code which only runs when it is called.
#Creating a Function & Calling a Function
def first_funtion():
    print("Function Called")
first_funtion()
# Parameters
def add(num1,num2):
    addition=num1+num2
    return addition
def sub(num1,num2):
    sub=num1-num2
    print(sub)
#Arguments
print(add(5,6)*4)
print(add(2,4))
sub(5,1)
def student(fname,lname,age):
    print("My name is",fname,lname,". My age is",age)
student("Muhammad","Zubair",25)
#Arbitrary Arguments, *args
def students_list(*std):
    for i in std:
        print(i)
students_list("Ali","Zubair","Umar","Aqsa","Amina")
students_list("akram","numan")
#Keyword Arguments
print(add(num2=23,num1=10))
#Arbitrary Keyword Arguments, **kwargs (recive dictionary)
def akfun(**dic):
    for i in dic:
        print(i)
        print(dic[i])
akfun(std1="Ali",std2="Umar",std3="Waseem")
#Default Parameter Value
def dfun(city="Lahore"):
    print("My City is",city)
dfun()
dfun("Multan")
#Passing a List as an Argument
list1=["Ali","Zubair","Umar","Aqsa","Amina"]
list2=["Umar","Aqsa","Amina"]
def list_std(list_s):
    for i in list_s:
        print(i)

list_std(list1)
list_std(list2)
# Return Values
def mul(num1,num2,num3):
    return num1*num2*num3
result=mul(3,5,6)
print(result)
#The pass Statement
def new():
    pass
new()
#Recursion function can call itself (Loop with out Loop)
def fat(num):
    if num==1:
        return 1
    else:
        return (num*fat(num-1))
print(fat(3))
