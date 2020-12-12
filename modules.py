from colorama import init
from termcolor import colored
#----Notes on Modules----

#writing code in one file and then using that within another file
#modules help to keep our python code small
#module is just another python file

#custom, builtin, external modules 
from random import choice, randint
print(choice(["pink", "purple", "blue", "yellow"]))

#----Custom Modules----
#same syntax from built in
#if it isnt in the right directory you need to reference the path to the file

#calling init because this strips the ANSI escape sequences and replaces with wind32 calls
init()

print(colored("My Dog is Rad!", "white", "on_blue"))

#__name__ returns the attribute __main__
#can use "if __name__ == "__main__" if you dont want what is Inside of the file to run on import but want to use the variables 
