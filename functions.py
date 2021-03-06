#Lets get down with functions
#function is a proccess for executing a task (making code procedures reusable)
#DRY: dont repeat yourself /Wet: writes everything twice

#just small example for syntax
def first_function():
    print("Testing Testing 1, 2, 3...")
#must call
first_function()

#return 
def return_function():
    #remember that the return exits the function
    return 2*2
num = return_function()
print(num)
#same as two other lines above without variable
print(return_function())

#creating little flip coin function as an example
from random import random

def flip_coin():
    #make a number (note this random() generates num between 0 and 1)
    if random() > 0.5:
        return "Heads"
    else:
        return "Tails"
print(flip_coin())

#starting to practice with perameters
def square(num):
    return num**2

#as a side note this way of writing the input doesnt control for any errors
#if a user puts something that isnt a number we will get an error
user_num = int(input("What do you want to square? "))
print(f"Okay the square of {user_num} is {square(user_num)}")

#multiple perameters
def combine_names(a,b):
    return a + " " + b
print(combine_names("First_Name", "Last_Name"))

#"arguments" are what we pass into a "parameter" of a function

#perameters having defaults
def combine_names2(a="First",b="Last"):
    """just returns a combined first and last name"""
    return a + " " + b
print(combine_names2())

#an example of using default keword arguments
print(combine_names2(b="Lebleu", a="Emerson"))

#some_function.__doc__ will give us the documentation of functions