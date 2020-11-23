# changes various units into new units

end_program = False

# conversions to universals: length/cm, Weight/g, Volume/ml
length = {
    "feet": 30.48,
    "inches": 2.54,
    "miles": 160934.4,
    "kilometers": 100000,
    "yards": 91.44,
    "meters": 100,
    "centimeters": 1}
weight = {
    "pounds": 453.59237, 
    "stone": 6350.29317,
    "kilograms": 1000, 
    "grams": 1, 
    "ounces": 28.3495231}
volume = {
    "fluid ounces": 29.5735295,
    "cups": 236.588236,
    "table spoons": 14.7867648,
    "tea spoons": 4.92892159,
    "quarts": 946.352945,
    "gallons": 3785.41178,
    "pints": 473.176472,
    "milileters": 1,
    "leters": 1000}

while end_program != True:
    # gather the data
    value = float(input("Measurement: "))
    starting_units = input("Starting units: ")
    ending_units = input("Convert To: ")

    # making appropriate conversions
    if starting_units in length and ending_units in length:
        value = value * length[starting_units]
        value = value / length[ending_units]
        value = round(value, 3)
        print(f"{value} {ending_units}")
    elif starting_units in weight and ending_units in weight:
        value = value * weight[starting_units]
        value = value / weight[ending_units]
        value = round(value, 3)
        print(f"{value} {ending_units}")
    elif starting_units in volume and ending_units in volume:
        value = value * volume[starting_units]
        value = value / volume[ending_units]
        value = round(value, 3)
        print(f"{value} {ending_units}")
    else:
        print("Sorry somehting is wrong with your units?")

    # stop or continue?
    end = input("Quit(y/n): ")
    end = end.lower()
    if end == "y":
        end_program = True
    else:
        end_program = False
