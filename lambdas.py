#Lamdas & Built in functions

#Lamdas are 
def square(num):
    return num*num

#one line functions, automatically returned (you can store in variable but typically no)
lambda num: num*num
#most common use case: when you are using within a function such as creating a button reaction

#map is often used with lambdas map accepts function and then an iterable 
numbers = [2,4,5,6,7,3,4,5,2,3,4,5]
square = map(lambda num: num*num, numbers)
print(list(square))

#filter is like map but rather than looping it is filtering filter is T/F
l = [1,2,3,4,5,6,7,8]
evens = list(filter(lambda x: x%2==0, l))
print(evens)

#list comprehension is better for sure but we need to know that there are these Lambdas/map/filter

#there are many built in functions

#all() takes an iterable and returns true if all elements are truthy
#any() returns true if any of the elements are truthy

#use generator expressions, if you dont need a list they are lighter

#SORTED()
#sorted() //different from sort// .sort() sorts in place, sorted sorts but not in place
#can also use sorted(x, reverse=True)

#can use on dictionaries sorted(x,key=xxvarious_possibilities can be a lambda as well)

#MAX() & MIN()
#can give iterable and will give the maximum/minimum
#can use functions within max/min to make more specific

#reversed() takes iterable and returns the reverse use reversed when you are iterating over 
#in reverse

#abs() absolute value
#in math so you must import math then math.fabs(-4) converts to float then give ab val
#sum(iterable,start) some iterable, start will tell it where to start what number to add these nums to
#round() specify the num of didgets
#zip() you zip together two lists into pairs (can be converted to dictionary or list returns tuple)
#can use the *argument to use sip to unpair things will create two seperate tuples

