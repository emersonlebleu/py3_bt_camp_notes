# Lists (other languages call them Arrays)
# collection of items, they have an order
# data structure: way of "structuring" or organizing data

shopping_list = [
    "banana",
    "apple",
    "onion",
    "soap",
    "broccoli",
    "tofu",
    "tortillas"]

#accessing the items
my_string = ""

#this is basically what .join() method would have done
#could have used a while loop as well which is prob the thing to do
for item in shopping_list:
    my_string += item+", "
print(my_string[0:len(my_string)-2])

#adding so we can see that it is the same
my_string2 = ", ".join(shopping_list)
print(my_string2)

#doing this a while loop
index = 0
my_string3 = ""
while index < len(shopping_list):
    my_string3 += shopping_list[index]+", "
    index += 1
print(my_string3[0:len(my_string3)-2])

#just printing with the index position
index = 0
print(f"Index: {index} Len Shopping list:{len(shopping_list)}")
while index < len(shopping_list): 
    print(f"{index}: {shopping_list[index]}")
    index += 1

print(f"Index: {index}")