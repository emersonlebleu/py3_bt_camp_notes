#----notes on debugging lesson----

#common Errors

#SyntaxError
    #something that python can understand, usually a typo

#NameError
    #occurs when a variable hasnt been defined

#TypeError
    #mismatch of data types and operation or function

#IndexError
    #using inappropriate index reference 

#ValueError
    #correct type, but not the right value like putting a string with char instead of num into a int() function

#KeyError
    #if you try to find something in a dict with a key that isnt in there

#AttributeError
    #variable doesnt have a certain attribute (or some method)

#Raising Errors (Exception): if you are creating modules or something that others are going to use this is a good practice
#example: you should use the proper type of error
# ---raise ValueError("This is a value error try something else")---

#try and except blocks
#can use try: /except: then you can try out something without breaking the whole thing usually you want to except a certain type of error

#----full possibility ----
# try:
    #Something
# except:
    #if not that try do this
    #you can have multiple of these
# else:
    #when except doesn't run
    #put a break here to break out if you are using this in a loop in user input
# finally:
    #funally runs no matter what

#----PDB: Python Debugger----
#the below can give an unreachable code message but it is just telling us that this does nothing at the moment... which it does
import pdb; pdb.set_trace()
#just a test
print(2 + 4)
print(3*4)
#Common Commands:
#l (list)
#n (next line)
#p (print)
#c (continue-finishes debugging)

#note you might get variable names that end up conflicting but you can use p then the name "c" for instance


