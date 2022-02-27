#while and for loops

#1_while loops
# A mother takes her child to school daily until the child is muture enough to go by himself. Hint: the maturity age is 10
# x=0
# while (x<=10):
#     print(x)
#     x=x+1

# for loop
# for x in range(5,10):
#     print(x)
 

 #array
from ast import Continue


days = [ "Mon", "Tue", "Wed","Thu","Fri","Sat","Sun"]
for d in days:
    # if (d=="Fri"): break       #loop stops 
    # print(d)
    if (d=="Fri"):continue
    print(d)