# ~~~~~~~~~~~~~~~~~~~~~~~~~~ Lists ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# A list also known as an array in other programming languages, is a data type that allows you to hold groups of values.
# Think of a list like a dresser with multiple drawers in which each drawer stores some information. Lists are created with values
# inside of square brackets [], where each value is seperated bya comma. After a list is created, in can still be upated by adding values and/or by deleting values.
# An empty list is simply [].

# In Python, the elements of a list do not have to be of the same date type. A list can be a moxture of any Python data types, including, tuples, strings, numeric, and even a list itself.

# Example:
mages = ['Rozen', 'KB', 'Oliver']
my_list = ['4',['list','in','a','list'],987]
empty_list = []

# Another cool feature of lists in python is that you can combine them together and duplicate values easily, by using + and * operators, If you 'add' lists together, it will 
# create a new list that contains all the values of both of the arrays! Likewise, if you 'multiply' a list by a whole number it will copy all of the values that many times, and make a 
# new list with all the copied values.

# Example:
fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables) # Output: ['apple', 'banana', 'orange', 'strawberry', 'lettuce', 'cucumber', 'carrots']
salad = 3 * vegetables
print(salad) # Output: ['lettuce', 'cucumber', 'carrots', 'lettuce', 'cucumber', 'carrots', 'lettuce', 'cucumber', 'carrots']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ List Manipulation ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

names = ["Tim", "Jon", "Dan"]
# Access the index of 0 and print the value
print(names[0])  # Output: Tim
# Access the index of 1 and print value
print(names[1]) #Output : Jon
# Access the index of 2 and print the value
print (names[2]) #Output : Dan

# Replace "Tim" with "Joan"
names[0] = "Joan"
print(names) #Output: ["Joan", "Jon", "Dan"]
# Store the value "Joan" in a temp variable
top_name = names[0]

# Replaces the value at index 1
# with whatever value is at index 0
names[1] = names[0]
print(names) #Output: ["Joan", "Joan", "Dan"]

# ~~~~~~~~~~~~~~~~~~~~~~~~ Appending Values to a List 

# You can use .append to append a new item onto the end of a list. You can pass any data type into this function

#Example
nums=[1,2,3,4,5]
nums.append(99)
print(nums) #Output: [1,2,3,4,5,99]

# ~~~~~~~~~~~~~~~~~~~~~~~ Slicing

# It's useful to know that Python uses the syntax [:] to return a copy of some portion of a list, constrained by specified indices. This is called slicing and it can be useful if:

# * You want to use a copy of the list so you don't have to change the original
# * Want to only use a portion of a list

# The starting index and ending index should be seperated by the : character.

# Example

words = ["start", "going", "till", "the", "end"]
# Sub-ranges (portions) of the list 
print(words[1:]) # Output: ['going', 'till', 'the', 'end']
print(words[:4]) # Output: ['start', 'going', 'till', 'the']
print(words[2:4]) # Output: ['till', 'the']

#Making a copy of a List 
copy_of_words = words[:]
copy_of_words.append("magic") # Only appends the copy
print(copy_of_words) # Output: ['start', 'going', 'till', 'the', 'end', 'magic']
print(words) # Output: ['start', 'going', 'till', 'the', 'end'] 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Built-in Functions for Lists ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# len(sequence) retruns the length(number of items) in a sequence
# Example
ex_list = ['Hello', 23, 'Roger']
print(len(ex_list)) # Output: 3

# max(sequence) returns the highest value in a sequence
# Example
ex2_list = [23,100,202]
print(max(ex2_list)) # Output: 202

# min(sequence) returns the lowest value in a sequence
# Example
ex3_list = [2,44,77,23,5,1]
print(min(ex3_list)) #Output: 1

#sorted(sequence) returns a sorted sequence
# Example
ex4_list = [333,79234,2,4564,3,6564,44,6]
print(sorted(ex4_list)) # Output: [2,3,6,44,333,4564,6564,79234]

# ~~~~~~~~~~~ List-Specific Methods

# list.append(value) appends a value to the end of the list
# Example
list1 = [1,3,4,5]
list1.append(7)
print(list1) #Output: [1,3,4,5,7]

# list.pop(index)
# Example 
list2 = [2,4,6]
list2.pop()
print(list2) # Output: [2,4]

# list.index(value) returns the index(position) of the given value if it exists in the list and raises an error if it does not.
# Example
list3 = [1,3,5,6]
print(list3.index(3)) #Output: 1

# list.reverse() reverses the order of the elements, in place (meaning it changes the same array instead of returning a new one)
# Example
list4 = [3,4,5,6,7,8]
list4.reverse()
print(list4) #Output: [8,7,6,5,4,3] 

# list.sort() sorts the items in order of least to greatest, or alphabetically for strings, in place (meaning it changes the same array instead of returning a new one)
#Example
list5 = [6,3,9,12,55,23,53,90]
list5.sort()
print(list5) #Output: [3,6,9,12,23,53,55,90]

