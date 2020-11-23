my_list1 = (1, 2, 3, 4, 5, 6)
word = "SaltLakeCity"
my_range1 = range(1,21,2)
my_range2 = range(1,6)

#for loops
#for item in iterable_object:
#   Do something with item

for char in word:
    print(char)

for num in my_range1:
    print(f"Sheep Number {num}")

#ranges are typically only used with for loops

#while loops
#while a condition is truth-y
my_response = None
while my_response == None:
    my_response = input("Enter Name: ")
print(f"Your name is {my_response}")

#break 
color = input("What is your favorite color? ")
while color != "orange":
    color = input("Lame! pick again: ")
    if (color == "Q"):
        break 