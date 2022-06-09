"""     4.1 String in Python    """
#Assign String to a Variable
name="My name is Muhammad Zubair"
print(type(name))
print(name)
#Multiline Strings
mul_Str="""First line is there 
2nd Line is there"""
print(mul_Str)
#Strings are Arrays
print(name[8])
#String Length
print(len(name))
#Check String
if "is" in name:
    print('Yes is is there')
#Check if NOT
if "Youtube" not in name:
    print('No there is no Youtube...')
#Slice From the Start
print(name[3:])
#Slice To the End
print(name[3:7])
#Upper Case
print(name.upper())
#Lower Case
print(name.lower())
#Remove Whitespace
print(name.strip())
#Replace String
print(name.replace("Zubair","Ali"))
#Split String
print(name.split())
#String Format
my_laptop="{1} laptop is {0} X360"
name_laptop="HP"
my_var="MY"
print(my_laptop.format(name_laptop,my_var))
"""String Methods"""
#capitalize()
print(name.capitalize())
#casefold()
print(name.casefold())
#center()
print(name.center(100))
#count()
print(name.count("Zubair"))
#endswith()
email="mzubair@gmail.com"
print(email.endswith(".com"))
if email.endswith(".com"):
    print("Yes your email format is correct")
else:
    print("Please enter .com at the end of your email address")
#find()
print(name.find("i"))
#format()
my_laptop="{1} laptop is {0} X360"
name_laptop="HP"
my_var="MY"
print(my_laptop.format(name_laptop,my_var))
#index()
print(name.index("Z"))
#isalnum()
#isalpha()
#islower()
print(name.islower())
#isnumeric()
print(name.isnumeric())
#isprintable()
print(name.isprintable())
#isspace()
space=" "
print(space.isspace())
#istitle()
print(name.title())
#isupper()
print(name.isupper())
#join()
list=['ali','umer','waseem']
print(" ".join(list))
#ljust()
ali="ali"
print(ali.ljust(20))
print(ali.rjust(20))
#lower()
print(name.lower())
#maketrans()
newname=name.maketrans('Z','U')
print(name.translate(newname))
#partition()
print(name.partition("Zubair"))
#replace()
#split()
print(name.split())
#splitlines()
print(name.splitlines())
#startswith()
print(name.startswith("My"))
#swapcase()
print(name.swapcase())
#title()
print(name.title())
#zfill()
zf="20"
print(zf.zfill(10))