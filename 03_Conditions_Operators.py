"""Conditions and If statements
    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b"""
a=130
b=20
if a>b:
    print("Yes A is Greater")
#Indentation
#If else
num1= int(input())
num2= int(input())
if num1>num2:
    print("Number 1 is greater then Number 02")
elif num1==num2:
    print("Number 1 is equal to Number 2")
elif num1<num2:
    print("Number 2 is greater then Number 1")

#Short Hand If
if num1==num2: print("Number 1 is equal to Number 2")
#Short Hand If ... Else
print("Number 1 is greater then Number 02") if num1>num2 else print("Number 2 is greater then Number 1")
#Nested If
gender = input("Enter your Gender Male or Female = ")
if gender=="Male":
    print("Now You Can Enter your Age")
    age=int(input())
    if age>=20:
        print("You Are Allowed")
    else:
        print("Less then 20 year old are not allowed")
else:
    print("Females not Allowed")
#The pass Statement
verb =10
if verb>12:
    pass

#Operators
#Arithmetic operators
'''
Operator 	Name 	        Example 
+ 	        Addition 	    x + y
- 	        Subtraction 	x - y
* 	        Multiplication 	x * y
/ 	        Division 	    x / y
% 	        Modulus 	    x % y
**      	Exponentiation 	x ** y
//      	Floor division 	x // y
'''
num1=int(input("Enter your First Number = "))
num2 = int(input("Enter your 2nd Number = " ))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1**num2)
print(num1//num2)
#Assignment operators
'''
Operator 	Example 	Same As 	
= 	        x = 10   	x = 10 	
+=      	x += 2 	    x = x + 2 	
-= 	        x -= 2  	x = x - 2 	
*=      	x *= 2  	x = x * 2 	
/= 	        x /= 2  	x = x / 2 	
%= 	        x %= 2 	    x = x % 2 	
//=     	x //= 2 	x = x // 2 	
**=     	x **= 2 	x = x ** 2 	
'''
x = 10
#x=x+2
x+=2
print(x)
#Comparison operators
"""  Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b"""
num1=int(input("Enter your First Number = "))
num2 = int(input("Enter your 2nd Number = " ))
if num1 >= num2:
    print("Greater Or Equal")
#Logical operators

''''
Operator 	Description 	                                                          Example 	
and  	    Returns True if both statements are true 	                            x < 5 and  x < 10 	
or 	        Returns True if one of the statements is true 	                        x < 5 or x < 4 	
not 	    Reverse the result, returns False if the result is true 	            not(x < 5 and x < 10)
'''
age=int(input("Enter Your Age: "))
if not(age >=18 and age<=30):
    print("You Are Allowed")
if age==20 or age==30:
    print("Allowed")
#Identity operators
a=10
b=12
print(a is not b)
#Membership operators
"""
Operator 	 	Example 	
in  	 	   x in y 	
not in 	 	  x not in y
"""
name= "My name is Capra Code"
print("youtube" not in name)
list1=["ali","umer","waqar"]
print("ali"in list1)
#Bitwise operators
a=10
b=4
print(a&b)
#Take two int values from user and print greatest among them.
num1=int(input())
num2=int(input())
if num1>num2:
    print("Number 1 is greater that is ",num1)
elif num2>num1:
    print("Number 2 is greater that is ",num2)
"""Write a program to check whether a person is eligible for voting or not. (accept age from user) """
age= int(input())
if age>=18:
    print("You Are Eligible for voting")
else:
    print("You Are Not Eligible for voting")


#Write a program to check whether a number entered by user is even or odd.
num1= int(input("Enter a Numner = "))
if num1%2==0:
    print("Your Number is Even: " ,  num1)
else:
    print("Your Number is odd: " ,  num1)

#Write a program to check whether a number is divisible by 7 or not
num1= int(input("Enter a Numner = "))

if num1%7 == 0:
    print("Your Number is divide able by 7: " ,  num1)
else:
    print("Not Divide able: " ,  num1)

num1= int(input("Enter a Numner = "))
print(num1%10)