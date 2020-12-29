#----CSV: Comma Separated Values----#
#you can read them in like typical files but it is better to use a module built to handle
#that type of data

#--reader--#
#lets you iterate over rows as a list

#--DictReader--#
#iterates over rows as ordered dictionaries

from csv import reader
with open("fighters.xls") as file:
    csv_reader = reader(file)
    for row in csv_reader:
        print(row)