#printing hello world and what's up as a strings
print("hello world")
print("what's up")


#Working with Operators
Joseph_age = 3
Age_at_kindergarten = 5

if Joseph_age < Age_at_kindergarten:
    print("Joseph should be in pre-school")
elif Joseph_age == Age_at_kindergarten:
    print("Enjoy Kindergarten")
else:
    print("Thomas should be in another class")


#At age 5
    Joseph_age = 5
Age_at_kindergarten = 5

if Joseph_age < Age_at_kindergarten:
    print("Joseph should be in pre-school")
elif Joseph_age == Age_at_kindergarten:
    print("Enjoy Kindergarten")
else:
    print("Thomas should be in another class")


#At age 7
    Joseph_age = 7
Age_at_kindergarten = 5

if Joseph_age < Age_at_kindergarten:
    print("Joseph should be in pre-school")
elif Joseph_age == Age_at_kindergarten:
    print("Enjoy Kindergarten")
else:
    print("Thomas should be in another class")


#Creating Functions
def print_Mary():
    text = "Mary has a great channel"
    print(text)
    print(text)
    print(text)
print_Mary()


#Passing values into a Function
def print_Mary(text):
    print(text)
    print(text)
    print(text)
print_Mary("Mary has a great channel")


#Putting If statement within a Function
def school_age_calculator(age, name):

    if age < 5:
        print("Enjoy the time!", name, "is only", age)
    elif age == 5:
        print("Enjoy kindergarten", name)
    else:
        print("They grow up so fast!")
school_age_calculator(3, "Asa")


#At age 5
def school_age_calculator(age, name):
  
    if age < 5:
        print("Enjoy the time!", name, "is only", age)
    elif age == 5:
        print("Enjoy kindergarten", name)
    else:
        print("They grow up so fast!")
school_age_calculator(5, "Asa")


#At age 7
def school_age_calculator(age, name):
  
    if age < 5:
        print("Enjoy the time!", name, "is only", age)
    elif age == 5:
        print("Enjoy kindergarten", name)
    else:
        print("They grow up so fast!")
school_age_calculator(7, "Asa")


#Getting values back fron a Function
def Add_ten_to_age(age):
    New_age = age + 10
    return New_age
How_old_will_i_be = Add_ten_to_age(3)
print(How_old_will_i_be)


# Creating Loops
# While
x = 0
while(x < 5):
    print(x)
    x = x+1


#For
for x in range(5, 15):
    print(x)


Days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for d in Days:
    print(d)


#Break
for d in Days:
    if(d == "Thu"):
        break
    print(d)


#Continue
for d in Days:
    if(d == "Thu"):
        continue
    print(d)


#printing the value of pie
import math
print("pi is", math.pi)