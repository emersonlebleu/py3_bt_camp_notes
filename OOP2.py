#----OOP2----

#---Inheritance---
#you can have different classes that inherit from a base (or parent) class

#---super() in the init of the current class can allow us to use the variables from the parent class

#--Polymorphism--
#the idea that an object can take on many forms
#the same class method works differently for different classes
#the same operation (method) works for different kinds of objects

#---magic methods--
#__add__()
#__len__
from copy import copy

class Human: 
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    def __repr__(self):
        return f"Human named {self.first} {self.last} age {self.age} years"
    def __len__(self):
        return self.age
    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="Newborn", last=self.last, age=0)
        return "You can't add that!"
    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "Can't Multiply" 

e = Human("Emerson", "Lebleu", 28)
m = Human("Mandy", "Lebleu", 28)

print(e)
print(len(e))
print(e+m)

twins = (e+m)*2
twins[0].first = "Chad"
twins[1].first = "Chet"
print(twins)

#grumpydict
class GrumpyDict(dict):
    def __repr__(self):
        print("None of your business")
        return super().__repr__()
    def __missing__(self, key):
        print(f"You want {key}? Well it isnt here")
    def __setitem__(self, key, value):
        print("You want to change the dictionary?")
        print("Ugh fine...")
        super().__setitem__(key, value)
    def __contains__(self, item):
        return "Nope not in here.."

data = GrumpyDict({"first":"Joe", "animal":"dragon"})
print(data)
data["city"] = "Tokyo"
print(data)
"city" in data