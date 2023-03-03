print("Hello World")

x= "Hello Python"
print(x)

y = 42
print(y) 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Pass ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# If we start a code block, there must be at least one line of indented code immediately following. 
# If we try to run a file with a hanging code block, we'll get a syntax error. 
# Luckily, Python has provided us with the pass statement for situations where we know we need the block statement, but we aren't sure what to put in it yet.

class EmptyClass:
    pass

# for val in my_string:
#     pass

# The pass statement is a null operation; nothing happens when it executes. 
# The pass is almost never seen in final production, but can be useful in places where your code has not been completed yet.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Data Types ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Primative Data Types

# These are the basic building blocks of a language. Most Languages have these in common

# *Boolean Values* - Assesses the truth value of something. It has only two values: True and False (Note the upper T and F)
is_hungry = True
has_freckles = False

# *Numbers* - Intergers (whole numbers), floating point numbers(commonly known as decimal numbers), and complex numbers
age = 35 # Storing an Interger
weight = 160.57 # storing a float

# *Strings* - literal text
name = "Joe Smith"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Composite Types 

# These are collections composed of the above primative types.

# *Tuples* - A type of immutable data and can hold groups of values. Tuples can contain mixed data types.

dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0]) # output: Bruce
# dog[1] = 'dachshund' # ERROR: cannot be modified ('tuple' object does not support item assignment!!)

# *Lists* - a type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.

empty_list = []
mages = ['Rose', 'Sabrina', 'Chrisma']
print(mages[2]) # Output: Chrisma
mages[0] = 'Jerry'
mages.append('Jenny')
print(mages) # Output : ['Jerry', 'Sabrina', 'Chrisma', 'Jenny']
mages.pop()
print(mages) # Output : ['Jerry', 'Sabrina', 'Chrisma']
mages.pop(1)
print(mages) # Output : ['Jerry', 'Chrisma']

# *Dictionaries* - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values. 

empty_dict = {}
new_kitten = {'name': 'Whiskers', 'age': 2, 'weight': 8.3, 'likes_mice': False}
new_kitten['name'] = 'Snowball' # Updates if the key exsists
new_kitten['hobbies'] = ['sunbathing', 'hunting'] # Adds a key-value pair if the key doesn't exist
print(new_kitten) # Output: {'name': 'Snowball', 'age': 38, 'weight': 8.3, 'likes_mice': False, 'hobbies': ['sunbathing', 'hunting']}
w = new_kitten.pop('weight') # Removes the specified key and returns the value
print(w) # Output: 8.3 
print(new_kitten) # Output: {'name': 'Snowball', 'age': 2, 'likes_mice': False, 'hobbies': ['sunbathing', 'hunting']}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Common Functions

#If we are unsure of a value or variable's data type, we can use the type function to find out!

print(type(2.63)) # Output: <class 'float'>
print(type(new_kitten)) # Output <class 'dict'>

# For data types that have a length attribute(eg. lists, dictionaries, tuples, strings), we can use the len functions to get the length:

print(len(new_kitten)) # Output: 4 (the number of key-value pairs)
print(len('Coding is fun!')) # Output : 14

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Numbers ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# There are 3 basic types of numbers in Python.

# *int* - whole numbers, positive or negitive. example: 35
# *float* - decimal numbers, positive or negitive. example: 4.2
# *complex* - are a part of the real number system and are often referenced with the letter j. example: 1 + 3j **note** if you are unsure if you need to use them, it's safe to say you can ignore this data type.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Conversion

# All Python objects have data type methods we can use to convert muber types from one to another

int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)

print(int_to_float) # Output: 35.0
print(float_to_int) # Output: 44
print(int_to_complex) # Output: (35 + 0j) 

print(type(int_to_float)) # Output: <class 'float'>
print(type(float_to_int)) # Output: <class 'int'>
print(type(int_to_complex)) # Output: <class 'complex'> 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Random Number

#Python does not have a built in random number generator but has a random module instead

import random
print(random.randint(2,5)) # Output: random number between 2 and 5

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ STRINGS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ String Literals

# Strings are any sequence of characters (letters,numerals, ~($\#, etc.) enclosed in single or double quotes. 

print("This is a sample string") # Output: This is a sample string

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Concatenating Strings and Variables

# There are mulitple ways that we can print a string containing data from variables.

# The first is by adding a comma after the string, followed by the variable. Note that the comma is outside the closing quotation mark of the string.
#The print() function insterts a space between elements seperated by a comma.

name="Zen"
print("My name is", name)

# The second is by concatenating the contents into a new string, with a +

name ="Zen"
print("My name is " + name)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Type Casting or Explicit Type Conversion

# We may find ourselves wanting to change a value's data type from one type to another. 
# Python doesn't know how to add a string and a number, but it can add two strings together, so if we can cast the number as a string, then we will be able to "add" the two values together, like so:

# print("Hello " + 42) #Output : TypeError
print("Hello " + str(42)) #Output : Hello 42

# Another example may be receiving a string input from a user that we want to treat as a number:

total = 35
user_val = "26"
# total = total + user_val # Output: TypeError
total = total + int(user_val) 
print(total) # Output: total will be 61

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ String Interpolation ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# We can also inject variables into out strings, which is known as string interpolation. There are a few different ways this can be done.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ F- Strings (Literal String Interpolation)

# Python 3.6 introduced f-strings for string interpolation. To construct a f-string, place an "f" right before the opening quotation. Then within the string, place any variables within curly brackets.

first_name = "Lara"
last_name = "Croft"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ string.format()

# Prior to f-strings, string interpolation was accomplished with the .format() method.

first_name = "Rupaul"
last_name = "Charles"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age)) # Output: My name is Rupaul Charles and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name)) # Output My name is 27 Rupaul and I am Charles years old. 

# The two example print statements are provided to demonstrate that the format method reads the string from left to right, replacing the {} with the value of the arguments provided,
# in order. This means there should be the same number of sets of {} as there are arguments passed into the function.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ % - formatting ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# There is an ever older method of string interpolation that you may come across when troubleshooting or researching, so you should know about it. Rather than curly braces, the %
# symbol is used to indicate a placeholder, a %s for a string and %d for a number. After the string, a single % seperates the string to be interpolated from the values to be inserted into the string

#Example:
hw = "Hello %s" % "world" 
py = "I love Python %d" % 3
print(hw, py) # Output: Hello world I love Python 3

name = "Diana"
age = 27
print("My name is %s and I'm %d" %(name, age)) # Output: My name is Diana and I'm 27

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Built-In String Methods ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#.title()
x = "hello world"
print(x.title()) # Output: Hello World

#.upper()
y = "hello world"
print(y.upper()) # Output: HELLO WORLD

#.lower()
i = "HELLO WORLD"
print(i.lower()) # Output: hello world

#.count()
i = "Hello World"
print(i.count("o"))  # Output: 2

#.split()
i = "Hello World"
print(i.split("o")) #Output ['Hell', 'W', 'rld']

#.find()
i = "Hello World"
print(i.find("World")) #Output 6 