#list comprehension xxx for xxx in XXXX
#with conditional logic xxx for xxx in xxxx if xxx some condition OR
#using else: xxx if xxx condition else xxx for xxx in xxxx

#simple Example
nums = [1, 2, 3, 4]

multiples = [x*10 for x in nums]
print(multiples)

#another example also using .join()
name = "Emerson"
cap_name = [char.upper() for char in name]
cap_name = "".join(cap_name)
print(cap_name)

