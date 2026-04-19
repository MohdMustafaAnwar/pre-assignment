print('Hello, World!')
print("This is a simple script to demonstrate printing in Python.")

# Store some number
x = 10
x = 9 # Store final number
print("the value of X:", x)

#Single and Double Quotes
print('Hello, World!')
print("Hello, World!")

# Escape Sequences
print("Hi \"Python\"")
print('Hi "Python"')
print('Hi \'Python\'"')

print("Path: Users\mustafaanwar\Python Codes")
# print("Path: \Users\mustafaanwar\Python Codes")
print("Path: \\Users\mustafaanwar\Python Codes") # Use \ as start of an escape sequence

# Empty Line
print("Message 1")
print() # For empty line
print("Message 2")

# New Line
print("Message 3\n")
print("Message 4")

# New Line and Tab space
print("Message 5\n\n\nMessage 6")

print("Message 7\tMessage 8")

print("Your Learning Path:\n\t-Python Basics\n\t-Data Enginnering\n\t-AI")

# Triple Quotes - Allows us to write text in multiple line strings
print("""Your Learning Path:
\t-Python Basics
\t-Data Enginnering
\t-AI""")
# you dont need a \n now as """ triple quotes itself understands that writing anything on a new line is itself considered to be on a new line.

# Variables - Whenever we assign values to a variable it stores all this in a variables box with variable name and its value. So whenever we want this value it is taken out from there
x = 1
print("the value of x:", x)
x = 2 # Store final number
print("the value of x:", x)
y = x + 3
print("the value of y:", y)
print()

print("My name is Mustafa")
print("Mustafa is learning python")
print("Mustafa wants to become Python Expert")
#Variable name , value
name = "James"
print("My name is", name) # everytime a comma is added it means a space will also be created
print(name ,"is learning python")
print(name ,"wants to become Python Expert")
# Variables make updates super easy - one change updates everything
print()

# If you find yourself using the same value over and over, store it in a variable to make your code easier to change!
name = "Alex"
language = "Python"
print("My name is", name)
print(name ,"is learning", language)
print(name ,"wants to become", language, "Expert")

print()
email = "datawithmustafa.com"
print("info@", email)
print("support@", email)
print("www.", email)
# This adds space after the first word so there are three ways to remove it
# 1) Use +
print("1) Use +")
print("info@" + email)
print("support@" + email)
print("www." + email)
# 2) Use sep="" -> it tells python -> Dont add space between arguments
print("2) Use sep=""")
print("info@", email, sep="")
print("support@", email, sep="")
print("www.", email, sep="")
# 3) Use f-strings (Best practice - Cleanest and most modern way)
print("3) Use f-strings") 
print(f"info@{email}")
print(f"support@{email}")
print(f"www.{email}")

# INPUT Fn INPUT() - A built-in Python function that stops your program to get user input
# Using INPUT() alone reads the user's response but immediately discarded it. To keep the value, assign it to a variable!
name = input("Enter Your Name:")
print("You are", name)

# Hard-coded (static) value - fixed piece of data written directly into your code that never changes at runtime
country = "Germany" # this value is predefined before the execution
print(name, "comes from", country)

# DATA TYPES - Python needs to understand how to treat your values!
# Python automatically detect data types -> a=10 , b="Hello", c=True -> so Python sees values such as it sees 10 which is an integer so it stores 
# this value in a box named as 'a' according to its size. Similarly for other types also. Now if Python sees that there is again a = "ABC",  but this time its a string
# so it wont create a new box. Instead it would destroy the old box a=10 and make a new one a="ABC" which is a string box and stores it in its memory
# So its not liek Java where you have type declarations before each variable. Python is smart enough to understand all this

# a=5
# b="hi"
# y=a+b
# print("The value of y is:", y) Not Supported

