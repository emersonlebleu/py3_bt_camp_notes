#ask for age
#age 18-21 wristbands
#21+ you can drink
#too young
age = input("Hi how old are you? ")

if age:
    age = int(age)
    if age < 18: 
        print("Sorry you are too young :(")
    elif age < 21 and age >= 18:
        print("Okay take a wristband, enjoy the show")
    else:
        print("Come on in and you can drink!")
else:
    print("Please enter an age!")