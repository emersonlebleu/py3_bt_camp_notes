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

user_num = int(input("What do you want to square? "))
print(f"Okay the square of {user_num} is {square(user_num)}")