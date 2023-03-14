# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# A function is a named block of code that we can execute to perform a specific task. More simply, a function is a list of instructions that we can run at anytime
# and as many times as we would like. If we find something that we seem to be using over and over again, it might be best to have a way to streamline the process
# A Function has a name, takes in parameters, performs a series of instructions, returns something afterward. The advantages of using functions are: Reducing the 
# duplocation of code, breaking down complex problems into simpler pieces, improving the clarity of code. 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Syntax ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The def keyword signifies the declaration of a function. This indicates that the following code is a function and assigns a name to that function, so that we
# can call it later. Parameters are inputs the function is expecting and appear inside the parenthesis that follows a function name.

# Example
def add(a,b): # function name: 'add', parameters: a and b
    x = a + b # process
    return x # return value: x

# We have declared a function with the def keyword, named it add, and specified that it takes two inputs (parameters). If this is all we have in our file, 
# nothing would actually appear to happen if we ran it. To actually run the function, we must execute it by invoking or calling it. This is done outside of 
# the function using the function name followed by (). Inside the parenthesis are any values (arguments) the function is expecting as input.

#Example
new_val = add(3,5) # calling the add function, with arguments 3 and 5 
print(new_val) # the result of the add function get sent back to and saved into new_val, so we will see 8

# Once invoked, a function can give us an output. Some functions take an input and some functions don't give us an output. Even if no output is produced, 
# the code inside the function can alter the program - this is called a side effect. Based upon what we learned above, a function that doesn't return 
# anything would produce no output

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Parameters and Arguments ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# We define the input of functions using parameters. Functions can have as many parameters as we need, including 0. 

#Example 
def say_hi(name):
    print("Hi, " + name)

# Now we can invoke this function by calling it name and passing in the correct number of arguments:
say_hi('Michael') #Output: Hi, Michael
say_hi('Anna') #Output: Hi, Anna
say_hi('Joe') #Output: Hi, Joe

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Returning Values

# So far none of our functions had any value that we could hold onto. In many cases, we would want our function to return some sort of value that we can 
# use later in our program. The following concept is critical in understanding how to use functions correctly in your code:

# It is very important to remember the following: a function call is equal to whatever that function returns. This might not make sense until we see it in action.

#Example
def say_hello(name):
    return "Hello " + name
greeting = say_hello("Jimmie") # The returned value from say_hello function gets assigned to the 'greeting' variable
print(greeting) # Output: 'Hello Jimmie'

# Returning a value from a function allows us to store that value in a variable. In this example, we invoked the say_hello function with "Michael" and set it to the
# greeting variable. When we print greeting we see that it contains the returned value of the say_hello function - "Hello Jimmie".

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Default Parameters ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# With the functions we've written so far, we've had to provide the exact number of arguments specified when calling the function. However, if we'd lie to allow some of
# the parameters to be optional to the caller of the function, we can set defaults. Take the following function as an example. The purpose of the function is to take a
# name and a number and print "good morning {some_name}" to the terminal the given number of times. If no name or number is given, the name is blank and the number is 2, respectively.

# Example
def be_cheerful(name='', repeat=2): # Set defaults when declaring the parameters
    print(f"good morning {name}\n" * repeat)

be_cheerful() #Output: good morning (repeated on 2 lines) No arguments provided - the defaults are used

be_cheerful("Tim") #Output : good morning Tim (repeated on 2 lines) One unnamed argument provided - provided value is used as the value for the first parameter, and the second parameter's default is used

be_cheerful(name="Jon") # Output: good morning Jon (repeated on 2 lines) One named argument provided -  provided value is used as the value for the parameter of the same name and the other's default is used
be_cheerful(repeat=6) # Output: good morning (repeated on 6 lines)

be_cheerful("Ginny", 7) # Output: good morning Ginny (repeated on 7 lines) Both unnamed arguments provided - values assigned to parameters in order

be_cheerful(name="Joe", repeat=3) # Output: Good morning Joe (repeated on 3 lines) Both named arguments provided - values are assigned to associated parameter (order doesnt matter)

