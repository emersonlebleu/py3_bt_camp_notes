#the first functions file was quite long so I'm splitting it
#using the * and ** operator 
#also leverage dictionary and tuple unpacking

def my_tuples(*args):
    return args
print(my_tuples(2,3,4,5,6))

#just sums what is passed in
def sum_all(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(sum_all(2,56,34,2))

#using keword arguments in a dictionary: with **kwargs you can allow for someone to give KV pairs
def name_example(**kwargs):
    if "Emerson" in kwargs and kwargs["Emerson"] == "Name":
        return print(f"Hi Emerson")
    return print("Not sure who you are...")
name_example(Emerson="Name")
name_example(Bob="Name")

# Order matters, parameters, *args, default parameters, **kwargs

#unpacking example for tuples
def sum_all2(*args):
    total = 0
    for arg in args:
        total += arg
    return total
nums = [3, 34, 56, 78, 2]
#just put * in front of the name of the variable that needs to be unpacked
print(sum_all(*nums))

#you can use ** to unpack into keword agruments for a dictionary if you want to pass that into a func