# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Dictionaries ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# A Dictionary is another mutable sequence type that can store any number of Python objects, including other sequence types. 
# Dictionaries consist of pairs (called items) of keys and their corresponding values. While this data structure is known as a dictionary 
# in Python, you'll see the same structure referred to as an associative array or hash table in other languages. In general, hash table is 
# the most generic term.

# Characteristics of a Python dictionary:
# ~ A dictionary is an unordered collection of objects.
# ~ Values are accessed use a key (typically a string).
# ~ A dictionary can shrink and grow as needed.
# ~ The contents of dictionaries can be modified.
# ~ Dictionaries can be nested.
# ~ Sequence operations such as slice cannot be used with dictionaries.

# ~~~~~~~~~~ Keys VS Indexes

# Keys:
# ~ Keys are typically strings.
# ~ Keys are not in any sort of order, as dictionary values are NOT stored sequentially in memory.
# _ Dictionaries ONLY have keys.

# Indexes:
# ~ Indexes are always integers.
# ~ Indexes are ordered (least to greatest) as list and tuple values are stored sequentially in memory.
# ~ Dictionaries do not have indexes.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Creating Dictionaries ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Creating a dictionary in Python is a little like creating any other sequence. You've already learned about lists and tuples. While lists are enclosed by brackets
# - [], and tuples are enclosed by parenthesis - (), dictionaries are enclosed by braces - {}. Below are a couple of techniques you'll find useful when building dictionaries.

# Literal notation
person = {"first": "Maggie", "last": "Smithe", "age": 67, "is_a_witch": True}
capitals = {} # Create an empty dictionary

# ~ NOTICE ~ the keys in the example above are all strings, but the values are a varitety of types. Generally you will only use strings for your keys. You can think of them as
# label for the stored value.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Adding New Key-Value Pairs

# Dictionaries do not have a .append() method. You can add new values by setting a new key much like you would a variable.

#Literal Notation 
person = {"first": "Maggie", "last": "Smithe", "age": 67, "is_a_witch": True}
capitals = {} # Create an empty dictionary
capitals["eng"] = "London"
capitals["frn"] = "Paris"
capitals["dnk"] ="Copenhagen"

#In the examples above, we created two dictionaries in two different ways:

#    1. Using leteral notation. The key-value pairs are enclosed by curly brackets. The pairs are seperated by commas. The first value if a pair is a key, which is followed by a 
#    colon character and a value. The "first" string is a key and the "Maggie" string is a value. 

#    2. Creating an empty dictionary and adding some values. The keys are inside the square brackets, the values are located on the right side of the assignment.


# ~ LIST SYNTAX ~
# my_list[0]=4

# ~ DICTIONARY SYNTAX ~
# my_dict["string"] = some_value

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Changing or Updating Values

# Each key in a dictionary must be unique. If you make an assignment using an exsisting key as the index, the old value associated with that key is OVERWRITTEN by the new value.
# You can use this characteristic to an advantage in order to modify an exsisting value for an exsisting key. 

person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# Adds a new key value pair for email to person
person["email"] = "alovelace@codingdojo.com"
        
# Changes person's "last" value to "Bobada"
person["last"] = "Bobada"
print(person)

# ~ NOTICE ~ The syntax above is the same for adding a new value as it is for updating a value.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Testing for an Exsisting Key

# Sometimes you may want to test if a key already exists in the dictionary to know whether to add an inital value or replace an existing value.

# if some_key in my_dict:
    # update the value

# This also works with the not logical operator:
if "email" not in person:
    person["email"] = "newemail@email.com"
else:
    print("Would you like to replace your existing email?")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Accessing Values

# To access the values of a dictionary, you can use the familiar square brackets along with the jey to obtain its value. 
print(person["first"]) # Output: Ada
full_name= person["first"] + " " + person["last"]
print (full_name) # Output: Ada Bobada

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Removing Values

#There are 2 ways to remove a key:value pair from a dictionary 

value_removed = capitals.pop("eng") # will remove the key 'eng' and return its value
del capitals["frn"] # will delete the key and not return anything

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Multi-Line Syntax Too!

# You can write any dictionary's key-value pairs on multiple lines to make it easier to read, which is very useful for larger dictionaries. 

#Example 
person ={"first": "Martin", "last": "Ryans", "age":66, "is_organ_donor": True}

#.... can also be written like.....

person ={
    "first": "Martin",
    "last": "Ryans",
    "age": 66,
    "is_organ_donor": True
}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Common Built-in functions and Methods ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Python includes the following standalone functions for dictionaries:
# ~ len()- give the total length of the dictionary
# ~ str() - produces a string representation of a dictionary 
# ~ type() - returns the type of the passed variable. If passed variable is a dictionary, it will then retrun a dict type.

# Useful dictionary methods:
# ~ .clear() -removes all elements from the dictionary 
# ~ .get(key,default=None) - a safe way to get a value, if the key might not exist. Returns the value for the specified key or None(or a value you specify) if the
#                            key is not in the dictionary.
# ~ .update(pairs_to_update) - add and update multiple key-value pairs at once, by passing in another dictionary of the pairs to update and add.
