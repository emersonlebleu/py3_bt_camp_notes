#----OOP----
#OOP is a method o fprogramming that attempts to model some process or thing in the world as a "Class" or "Object"
#oop doesnt add functionality it is just a way of thinking and organizing your code
#may have the added benifit of helping you to think about your code at a higher level

#---Class---
#class is a blueplrint for an object, classes can contain methods, functions and attributes
#inheritance - some classes are related to overarching classes
#the bulk of understanding is knowing what should be a class

#---Object---
#instances that are constructed from a class blueprint

#---Abstraction---
#abstract away extra code to allow for a more intuitive understanding of the code
#hide the interworkings away

#---Encapsulation---
#goal is to encapsulate your code into locial hierarchical groupings
#grouping pulblic and private attributes and methosds into a class

#---Examples---

class User:
    #this is defining an instance when a new user is called and we want it to have these properties
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

user1 = User("Emerson", "Lebleu", 28)
print(user1.first_name + " " + user1.last_name)


