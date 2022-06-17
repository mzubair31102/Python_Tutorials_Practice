# A lambda function is a small anonymous function.
# Syntax lambda arguments: expression
x = lambda a,b,c:a+b*c
print(x(3,7,3))
# A lambda function can take any number of arguments,
# But can only have one expression.
# Why Use Lambda Functions?
# Use lambda function as an anonymous function inside another function.
def l_fun(num):
    print(num)
    return lambda num2,num3:num*num2*num3
c_fun=l_fun(4)
print(c_fun(5,5))