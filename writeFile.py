print("Type Filename")
filename = input(">")
print("We are going to erase ", filename)
print("Opening filename")
"""this will open the file if it exists
if file does not exist it will create new file"""
target = open(filename, 'w')

"""we will truncate data of file if file already
exists"""
print("Truncating the file")
target.truncate()

#Write three lines
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

#We are going to write these to the file
target.write(line1)
target.write(line2)
target.write(line3)

#And finally we close it
target.close()

