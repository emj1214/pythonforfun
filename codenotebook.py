#Python Code Notebook
# These are things I wanted to review form the CS1 textbook. I made it to chapter 7 before I got bored.

##Function
def first_function():
    print("hello")

first_function()

##Calling From a Library (using a function someone else wrote)
#from simplefunctions import print_date_and_time

#print_date_and_time()

##Functions That Take Params
#from simplefunctions import print_sqrt

#print_sqrt(4)
#print_sqrt(9)


##calling all functions from a library
#from cs1lib import *

##vars have no parentheses
meaning_of_life = 24
print(meaning_of_life)

##addition +
##subtraction - 
##multiplication *
##division with decimals /
##division with an integer result //
##modulus (gives remainder) %
##concat strings with +
##==, <=, >=, !=
##= is assignment operator, == is equal to 
##< and > can be used to alphabetize strings
##true>false
##don't use == to compare floats
##not looks for the opposite in a boolean
##use of and + or

##loops
i = 1
while i<15:
    i = i+1
    print(i)

##if and else, elif

##turn a value into a string => str(var)
##counts string length => len("string")
##turns string into number => int("123")
##float returns a number with a decimal (something you can't store as an int)

##randint = random integer
##uniform = random float

##coin flip program
from random import randint

heads = 1
tails = 2
count = 0

while count < 5:
    count = count + 1
    flip = randint(1, 2)
    if flip == heads: 
        print("Heads!")
    elif flip == tails:
        print("Tails!")
    else:
        print("there was an error???")

##global before a var makes it available outside of its given function
##return evaluates true or false

##call clear_timeouts before calling a timeout 
##set_timeout(function name, wait in millisecs, # of times to repeat)
