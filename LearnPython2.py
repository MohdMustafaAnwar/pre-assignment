# Data Types
a = 10 #int
b = 3.15 #float
c = "Hello" #str
d = 'Hi' #str
e = "1234" #str
f = True #bool
g = False #bool
# True and False are case-sensitive, they must start with a capital letter
h = None #NoneType -> #means "no value" , "nothing" or "unknown". It's used to show the absence of any data. So Python doesn't know which data type it is
i = "" #str -> #blank "" is a string value with no characters inside, it is not the same as None! Python knows its str data type
j = " " #str -> #Empty Space / white space " " is a string vlaue with 1 or more spaces, it is not same as None!

# id="mustafa"
# print(id.find("a"))

# nums = [1, 2, 3, 4, 5]
# print(nums.pop())

# type() - Build-in fn, returns the data type of a value, so you know what kind of object it is
text = 'hi'
number = 10
print(type(text))
print(type(number))

# len() - Built-in fn, gives the total count of items inside a value, helping you measure its length
print(len(text))

# upper() - Method of <class str> - Converts all letters in a string to uppercase
print(text.upper())

# bit_length() - Method of <class int> - returns the length of a number in binary
print(number.bit_length()) # it means it needs 4 bits to store the value 10

age = 10
height = 5.7
name = "Mustafa"
student = True
noValue = None

print("age:", age, "height:", height, "name:", name, "student:", student, "No Value:", noValue)
print(type(age), type(height), type(name), type(student), type(noValue))
print(len(name))

# Chapter 2 - Working with Strings