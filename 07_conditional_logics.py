# Logical Operators
# Equal to                  ==
# Not Equal to              !=
# greater than              >
# less than                 <
# less than or Equal to     <=
# greater than or equal to  >=
# ----------Logical Operators can be------Ture or False-----Yes or No----- 0 or 1-----------



#is 2 equal to 100
print(2==100)                           #   = is used for assigne the value whereas == is for "equal to"
# is 2 not equal to 100
print(2!=100)
# is 12=12
print(12==12)


# application of logical operators
rule= "this video is restricted for age 18"
required_age=18
age= 18
print("Your age is perfect ")
print(required_age==age )
print("Video Starts ")

# through input
rule= "this video is restricted for age 18"
required_age=18
age =input("What is your age? ")              # error here is due to the type/class of age. its string so convert it into integer first
age = int(age)
print(required_age==age )
print("Video Starts ")