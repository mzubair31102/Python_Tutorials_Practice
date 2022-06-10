
# The while Loop
n=5
while n>0:
    print(n)
    n=n-1
print("Bhoom")
x=1
while x<=100:
# The continue Statement
    x = x + 1
    if x==98:
        continue
    print(x)
# The break Statement
y=1
while y<10:
    """if y==7:
        break"""
    print(y)
    y +=1
# The else Statement
else:
    print("Loop Executed ")
# For Loops
# Looping Through a List
list1=["std1","std2","std3","std4"]
for i in list1:
    print(i)
# Looping Through a String
sting1="Channel Capra Code"
for x in sting1:
    print(x)
# Looping Through a Tuple
# Looping Through a Set
# Looping Through a dictionary
# The break Statement
list2=["std1","std2","std3","std4"]
for y in list2:
    if y=="std3":
        break
    print(y)
# The continue Statement
list2=["std1","std2","std3","std4"]
for y in list2:
    if y=="std3":
        continue
    print(y)
# The range() Function
for z in range(4,10,2):
    print(z)
# Else in For Loop
else:
    print("Executed")

# Nested Loops
list1=["std1","std2","std3","std4"]
books=["Math","Computer","Physics"]
for i in list1:
    print(i)
    for j in books:
        print(j)

# The pass Statement
for z in range(4,10,2):
   pass
# 1: Write a program to print first 10 odd numbers.
for i in range(1,21,2):
    print(i)
# 2: Write a program to print first 10 even numbers in reverse order.
for i in range(20,-1,-2):
    print(i)
# 3: Write a program to print table of a number accepted from user.
'''num = int(input("Enter Your Number: "))
for i in range(1,11):
    print(num," x ",i," = ",num*i)
    # 4: Write a program to find the factorial of a number.
num = int(input("Enter Your Number: "))
f=1
for i in range(1,num+1):
    f=f*i
print("Factorial of",num," = ",f)
    '''

# 5: Write a program to check whether a number is prime or not.

# 6: Write a program to print the following pattern
"""
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()