# this is a comment
"""
this is a multiline string
but can also be used as a multiline comment
"""
import webbrowser

# VARIABLES
weight = 20
name = "John Doe"
name = "Mark Lou"
weight = 20.5
output = ""

"""DATA TYPES:
   -NUMBERS:integers,float,complex
   -TEXT:strings str()
   -LIST:list ,set,tuple,dictionary
"""
# integer: int()
numberOne = 20
output = type(numberOne)  # checking data type
output = numberOne
""" ARITHMETIC OPERATORS:
   -ADD:sum
   -addition +
   -subtraction-
   -multiplication*
   -power()
   # division /
   -floor division//
   -modulus%


"""
x = 10
y = 12
output = x + y
output = x - y
output = x * y
output = x / y
output = x // y
output = x % y
x = 10
# x+=1
# x-=1
# x=x*3
# x/=9
# x%=3
# x**=3
"""
COMPARISON OPERATORS:
#     less than <
#  greater than >
# less than or equal to <=
# greater than or equal to >=
# 
"""
x = 100
y = 90
output = x < y
output = x > y
output = x >= y
output = x <= y
output = x > y

output = x != y
"""BOOLEAN OPERATORS:
   -and
   -or
   -not//
   """
fruit = "orange"
weather = "sunny"
output = (fruit == "orange") and (weather == "rainy")

# age=12
# weight=20.5

# output=(age>18) and (weight>5)
# output=(age<18) or (weight<5)

btemp = 20
rtemp = 30
output = (btemp < 30) and (rtemp > 20)

"""
STRINGS:
# list of characters2
# surrounded by either'' ,"" , """ """
# immutable
# 

"""
name = "John Doe"
output = name
output = name[
    1:8:4]  # slicing using step (It prints the letters after every four characters in the eight characters of JOHN DOE)
NAME = "PURPLE HIBISCUS"
output = NAME[1:15:4]

name = "Purple hibiscus"
# output=name.upper()
output = name.find("purple ")
output = name[14:]
output = name.count("i")
name = "Purple hibiscus"

location = "NAIROBI"
name = "Purple hibiscus"
# f string
output = "I am watching " + str(name) + " in " + location  # string concatenation
# f string
output = f"I am watching {name} in {location}"
"""
FUNCTIONS:
-DO STH (single purpose group of statements)
-types
   -lambda functions (anonymous function)
    -parameterized functions
    -non parameterized functions


"""
# lambda ;parameters; expression
summation = lambda a, b: a + b
output = summation(2, 3)


#     -parameterized functions
def greetings():  # defining a function
    print("hello")


greetings()  # CALLING A FUNCTION

# def washDishes():
# print("TAKE SOAP")
# print("WASH IT")
# print("RINSE")
# washDishes()
# parameterized functions
name = "JOHN DOE"


def welcomeHome(name):
    jina = name
    # print(f"Welcome home {name}")


# welcomeHome(name)
def student(name, age, course):
    studentID = f"{name} {age} {course}"
    print(f"Student is called {name} . He is {age} years old and does {course}.")


# student("ANNIE",12,"ENGINEERING (SOFTWARE)")

def books(book, date, when):
    print(f"Booking {book} {date} {when}")


books("amia", "2019", "2020")

"""
LIST:
   -lists
   -tuple
   -sets
   -dictionaries


"""
fruits = ["mango", "apple", "orange"]
output = fruits[1]
# for all in fruits:
#     print(all)

# replacing items in a string
students = ["charity", "linda", "maine", "mary"]
students[1] = "yolanda"
output = students
"""
# SETS:
A COLLECTION OF UNIQUE ITEMS
SO LIKE HAKUNA KUREPEAT VITU
IF AN ITEM APPEARS THRICE UKIPRINT ITAAPPEAR ONCE
EXAMPLE BELOW:
"""
books = {"mtu na watu", "my pain", "my people", "mtu na watu", "mtu na watu"}
print(books)
my_list = [10, 20, 30, 40, 50]
total = sum(my_list)
print(total)

# print(output)
