x=5                                     #integer
y=13.14                                 #float
z="Raja"                                #String
print(x,'its type is: ',type(x),y,'its type is: ' ,type(y),z,'its type is: ', type(z))

#implicit type conversion
x=x+y
print(x,'its type is: ',type(x))
y=x*y
print(y,'its type is: ',type(y))
# z=x*z
# print(z,'its type is: ',type(z))            #can't multiply a numeric with a non numaric
#explicit type conversion
age= input("What is your age? ")
age=int(age)
print(age, type(age)) 
#2nd way of this
age= input("What is your age? ")
print(age, type(int(age))) 