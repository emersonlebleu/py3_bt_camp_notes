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
print(return_function())