#----CSV: Comma Separated Values----#
#you can read them in like typical files but it is better to use a module built to handle
#that type of data

#--reader--#
#lets you iterate over rows as a list

#--DictReader--#
#iterates over rows as ordered dictionaries

# from csv import reader
# with open("fighters.xls") as file:
#     csv_reader = reader(file)
#     (csv_reader) #starts us after the headers so they dont print
#     for row in csv_reader:
#         print(row)

#--to remember, it gives you an iterator not a list etc automatically
# from csv import reader
# import csv
# with open("fighters.xls") as file:
#     csv_reader = reader(file)
#     data = list(csv_reader) 
#     print(data)

#with DictReader example
# from csv import DictReader
# from os import name
# with open("fighters.xls") as file:
#     csv_reader = DictReader(file)
#     for row in csv_reader: 
#         print(row["Name"])

#--Delimiter is what separates the values and can read files not sep by commas
##syntax: csv_reader = DictReader(file, delimiter="|")

from csv import writer, DictReader, reader
from os import read
# with open("dog_data.csv", "w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Name", "Breed", "Age"])
#     csv_writer.writerow(["Eli", "Boxer", 10])
#     csv_writer.writerow(["Carter", "Mutt", 7])
#     csv_writer.writerow(["Odin", "Pug", 0])
#     csv_writer.writerow(["Annie", "Poodle", 6])

with open("dog_data.csv") as file:
    csv_reader = reader(file)
    dogs = [[x.upper() for x in row] for row in csv_reader]

#since I already have an import statment i'm not having to write it again
with open("dog_data_caps.csv", "w", newline='') as file:
    csv_writer = writer(file)
    for dog in dogs:
        csv_writer.writerow(dog)  
