#---File I/O input output---#

#this is super important for data science
#also in web dev for CSV or HTML files
#reading and writing files, opening files, using "with" blocks
#json and CSV files

#can read a file with the open("file_name.ext") function (with whatever file name)

#some_file.read() reads to the end defaults to -1
#some_file.seek(position) puts the "cursor" wherever
#some_file.readline() reads for whatever line stops with new line character \n
#some_file.readlines() returns a list of lines in a list

#you also have to close the file close("some_file.ext")

#syntax example of with Block
#with open("somefile.txt") as file:
    #file.read()

#----Writing to Files----#
#still need to open a file
# with open("somefile.txt", "w") as file:
#   file.write("some stuff in here\n")
# the original stuff is overwritten with the "w" flag

#There are many flags to use for Open
#r no writing
#w overwrites
#a append adds to end doesnt overwrite (cannot add anywhere else)
#r+ reads and writes based on cursor but it will overwrite if you insert into a location



