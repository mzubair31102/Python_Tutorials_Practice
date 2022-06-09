#Creating a Function & Calling a Function
def myfun():
    print("Function Called")
myfun()
#Arguments
def newfun(name,email,number):
    print("My name is ",name,"My Email Address",email,"My Mobile Number",number)
newfun("Muhammad Zubair","email","0302")
#Arbitrary Arguments, *args
def afun(*tupleitem):
    print(tupleitem[2],tupleitem[1])
afun("Muhammad Zubair","email","0302")
#Keyword Arguments
def nfun(num1,num2,num3):
    print(num1,num2,num3)
nfun(num1="Ali",num2=23,num3="Umar")
#Arbitrary Keyword Arguments, **kwargs (recive dictionary)
def nnfum(**num):
    print(num["num1"],num["num2"])
nnfum(num1="umar",num2="zubair")
#Default Parameter Value
def d_fun(name="Zubair"):
    print(name)
d_fun()
d_fun("Umar")
#Passing a List as an Argument
def l_fun(names):
    for i in names:
        print(i)
users=["Ali","Zubair","Waseem","Usman"]
l_fun(users)
# Return Values
def n_f(x):
    return x*5
print(n_f(4))
#The pass Statement
def pass_fun():
    pass
#Recursion function can call itself (Loop with out Loop)
def r_fun(x):
    if(x>0):
        resutl=x+r_fun(x-1)
        print(resutl)
    else:
        resutl = 0
    return resutl
r_fun(7)