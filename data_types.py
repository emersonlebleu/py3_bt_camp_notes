#types of data in python
#variables in python are dynamically typed, meaning they can go from one data type to another
#languages such as C++ are statically typed, once they are a data type they stay that type and you define the type ahead of time

#bool = True or False
game_over = False
game_over = True
print(game_over)

#interger = number (non-decimal)
#float = number with decimal

#string = some unicode characters
my_name = 'Emerson'
print(my_name)
print('What did he think a "folder" was?')

#escape sequences for strings (lots of them look up on the python documentation)
print('Hello\nWorld')

#concatination
last_name = 'Lebleu'
print(my_name + " " + last_name)

#side note
numeral = 9
numeral += 9
print(numeral)

#f-string
odin_age = 5
answer = f"Odin's age is {odin_age} months"
print(answer)

#strings are indexed starting with 0
indexed_thing = "theraftisaweirdthing"
print(indexed_thing[0:5])

#can change something into a new data type by passing in the data type as a function
my_first_list = [2,4,6,6,7,8]
my_first_list = str(my_first_list)
print(type(my_first_list))
print(my_first_list)

##Data Structures: they store data within themselves##
#list = some ordered sequence of values
#dict = key value pairs
#tuple = immutible list
#None = Nothing python's version of null
x = None