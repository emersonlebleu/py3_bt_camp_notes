#just some dictionary stuff 
#dictionary gives key and value pairs that allows us to understand the info

#this is just a little practice dictionary and basic get
my_information = {
    "name": "Emerson",
    "has_dog": True,
    "number_of_dogs": 2, 
    "favorite_food": "Tacos", 
    "email": "emerson.lebleu@gmail.com" 
}

#note this works because input is already a string type
# search = input("What would you like to know?: ")

#make sure is in keys, note could just have done my_information
# if search in my_information.keys():
#     print(my_information[search])
# else:
#     print(f"Sorry, {search} is not something I know...")

#iterating over dictionarys
for k,v in my_information.items():
    print(f"Key:{k}, Value:{v}")

#dictionary methods
#.clear() gets rid of
#.copy() makes a clone
#pop(key)
#popitem() removes whatever... something random
#place to update.update(info to update with) (will also overwrite)
#{}.fromkeys()
new_user = {}.fromkeys(["name", "email", "last_name", "age"], None)
# print(new_user)

print(my_information.get("name"))

#dict comp
#{x:x for x in x}
{print(f"Key: {k}"):print(f"Val: {v}") for k,v in my_information.items()}
#practice with conditionals within dict comp
practice = {num: ("even" if num %2 ==0 else "odd") for num in range(1,20)}
print(practice)