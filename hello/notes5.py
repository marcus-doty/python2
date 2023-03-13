# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Loops ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ range()

# We can use Python's range function in conjunction with python for loops to repeat the same code many times with a number, 
# usually called i that represents an integer that changes. This is similar to for loops in other languages, but the syntax is a bit different. 
# The range() function can have between 1 and 3 arguments and creates a sequence of integers called a range object. We primarily use this for creating 
# loops that have a defined starting point and a stopping point for a sequence of integers.

# ~~~~~~~~~~~~~~~~~~~~~ Three ways to use range() in a for loop

# One Argument
for i in range(5):
    print(i) # Output: 0 1 2 3 4
# i starts at 0 by default, exits lopps when i is 5 (prints 4 but not 5), i increases by 1 each time by default

# Two Arguments
for i in range(2,7):
    print(i) #Output : 2 3 4 5 6
# i starts at 2, exits when i is 7 (prints 6 but not 7), i increases by 1 each time by default

#Three Arguments  
for i in range(2,16,3):
    print (i) #Output : 2 5 8 11 14
# i starts at 2, exits when i is 16 or larger than 16, increases by 3 each time

# Note that if you need to specify an increment other than +1 all three arguments are required.
# You may also start at a larger number and go down! To decrement (think going backwards) the step will be a NEGITIVE number to indicate i will get smaller each interation

# Examples 
for x in range(0,10,2):
    print(x) #Output: 0 2 4 6 8

for x in range(5,1,-3):
    print(x) #Output: 5 2

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ For Loops through Strings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Since a loop can be used on any sequence, you can access each value of a string individual with a loop.
# Example
for x in 'Hello':
    print (x) #Output: 'H', 'e', 'l', 'l', 'o'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ For Loops through Lists ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# If we want to iterate through a list, we could use the range function and send in the length of the list as the stopping value,
# but if we are not interested in the index values and want to just see the values of each item in the list in order, we can actually loop to get the values of the list directly!
# Example
my_list =["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print (i, my_list[i]) # Output: 0 abc, 1 123, 2 xyz

    # OR

for v in my_list:
    print(v) #Output: abc, 123, xyz

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ While Loops ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# While loops are another way of looping WHILE a certain condition is true
# Example
count = 0 
while count <= 5:
    print("looping - ", count) #Output: looping - 0, looping - 1, looping - 2, looping - 3, looping - 4, looping - 5
    count +=1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Else

# There are certain conditions that we give for every loop that we have, but what if the condition was not met and we still would like to do something if that happens?
# We can then use an else statement with our while loop.
#Example
y =3
while y > 0:
    print(y)
    y=y-1
else:
    print("Final Else Statement") # Output: 3 2 1 "Final Else Statement"
# Note that this else code section is only executed if the while loop runs normally and its conditional is false (whether we never entered the 
# while loop, or we did but eventually the conditional changed from true to false). If instead our while loop is exited prematurely because of a break 
# or return statement, then the else code section will never be executed.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Loop Control ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# We were introduced to control flow in the previous tabs with if and else statements. Loops, breaks, and continues are all a part of control flow as well. 
# Control flow is the cornerstone of most programming languages.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~ Break 

# The break statement exits the current loop prematurely, resuming execution at the first post-loop statement. The break statement can be used in both while and for loops.
# The most common use for the break is when some external condition is triggered, requiring a hasty exit from a loop.
# When loops are nested, a break will only exit from the innermost loop.

# Example 
for val in "string":
    if val == "i":
        break
    print(val) # Output: s, t, r
# Note: when the loop got to the letter "i", we stopped looping.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~ Continue

# The continue statement immediately returns control to the beginning of the loop. The other words, the continue statement rejects or skips all the remaining statements 
# in the current iteration of the loop, and continues normal execution at the top of the loop. The continue statement is very useful when you want to skip specific iterations but still
# keep looping until the end.

# Example
for val in "string":
    if val == "i":
        continue
    print(val) # Output: s, t, r, n, g
# Note: no i in the output, but the loop continued after the i