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

#----Class attributes----
#class attributes are shared by all members of the class
#used less often

#----Class Methods----
#concerned with the class itself not the specifics

#---__repr__---
#return the representation

#---Examples---

class User:
    
    active_users = 0

    @classmethod #didnt acctually call this below
    def display_active_users(cls):
        return f"{cls.active_users} active users"
    
    @classmethod #this one is more common working with CSV files
    def from_string(cls, data_str):
        first_name,last_name,age = data_str.split(",")
        return cls(first_name,last_name,int(age))

    #this is defining an instance when a new user is called and we want it to have these properties
    def __init__(self, first_name, last_name, age): #this is a method
        self.first_name = first_name #these are attributes
        self.last_name = last_name
        self.age = age
        User.active_users += 1
    
    def __repr__(self):
        return str({"first_name":self.first_name,"last_name":self.last_name,"age":self.age})
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def initials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}"

    def is_senior(self):
        return self.age>=65

user1 = User("Emerson", "Lebleu", 28)
print(user1.full_name())
print(user1.initials())
print(User.active_users)

user_data = "Tom,Welling,45"
user2 = User.from_string(user_data)
print(user2.full_name())
print(User.active_users)

print(user1)

