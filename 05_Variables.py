# Varibales are objects containing specific values
from re import T


x=5
print(x)

y="Raja Ali Dad"
print(y)

x=12
print(x)           # an update in value of x and new value will replace the previous one. update in code occurs from top to bottom.

x=14+x
print(x)
print(x,y)         # multi varibales in single line 
x,c= 22,21
print(x,c,y)


#Types of Variables or Class of Variables
z=12.14
#print(type(x,y,z))      we can't find multi types in signle line
print(type(x))
print(type(y))
print(type(z))
print()


# Rules to assign a Variable
# 1-  A variable name must start with a letter or the underscore character.
# 2-  A variable name cannot start with a number.
# 3-  A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
# 4-  Variable names are case-sensitive (name, Name and NAME are three different variables).
# 5-  The reserved words(keywords) cannot be used naming the variable. or any functional keywords
# 6-  Spaces are not allowed
# 7-  short and descriptive for ease
# 8-  Use lower case letters for ease
names_of_friends = "Ali", "Asad", "Mudassir"
print(type(names_of_friends))
del names_of_friends             # del deletes the variables
print(names_of_friends)
