#####################################
#  file processing in puython
#####################################
"""

Cheatsheet: File Processing
In this section, you learned that:

# You can read an existing file with Python:

with open("file.txt") as file:
    content = file.read()

# You can create a new file with Python and write some text on it:

with open("file.txt", "w") as file:
    content = file.write("Sample text")


# You can append text to an existing file without overwriting it:

with open("file.txt", "a") as file:
    content = file.write("More sample text")


# You can both append and read a file with:

with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()

"""
#how to read file in python

myfile = open("fruits.txt")
content = myfile.read()  # good idea to store the content in a variable because read operations leaves the cursor at the end of the file

print(content)      # by storing the content in a variable, we can print the content multiple times

# close the file
myfile.close()

print(content)  # print the content even when the file is already closed

#############################
# opening files using 'with'
# advantage: closing the file is automatic after the intended block is done
###################################################################3

with open("fruits.txt") as myfile1:
    content1 = myfile1.read()

print(content1)


# relative path

with open("./files/grocery.txt") as mygrocery:
    content2 = mygrocery.read()

print(content2)

##################################################
# writing to file
# this method overwrites the current file if it exists
# create the file if not existing
###################################################
with open("files/vegetables.txt", "w") as mygrocery2:
    mygrocery2.write("Tomato\nOnions\nLettuce\n")
    mygrocery2.write("Cucumber\n")

# writing -- append to existing file
# "a" option allows for append, but adding "+" allows to read also
# reset the cursor to position (0) by using seek(0)
######################################
with open("fruits.txt", "a+") as mygrocery3:
    mygrocery3.write("\nOkra")
    mygrocery3.seek(0)
    content3 = mygrocery3.read()

print(content3)



"""
# Lesson exercises:
# ex reading:  read bear.txt file and print the first 90 characters in it
# The file.read() method returns a string. You can use [:90] to extract the first 90 characters from that string.
##################################################################
with open("./files/bear.txt", "r") as my_bear:
    content3 = my_bear.read()

print(content3[:90])


# ex reading and processing:  define a function that gets a single character and filepath as parameters
#  then returns the number of occurences of that character in the file
###################################################3
def char_find(char, file_name):
    with open(file_name, "r") as myfile:
        content = myfile.read()
        return content.count(char)

# ex writing:  create a file name file.txt and write the text "snail"
#######################################################################3

with open("./files/file.txt") as myfile:
    myfile.write("snail")

# ex read and write:
# create a first.txt that contains the first 90 characters of bear.txt
#########################################################################
with open("./files/bear.txt", "r") as my_bear:
    content = my_bear.read()[:90]

with open("./files/first.txt", "w") as my_first:
    my_first.write(content)

# ex read and write append
# read content of bear1 and append to bear2
##################################################

with open("./files/bear1.txt", "r") as bear1:
    content = bear1.read()
    
with open("./files/bear2.txt", "a+") as bear2:
    #bear2.write("\n")
    bear2.write(content)


# append n times
# Create a "with" block where you open the file in 'a+' mode. Put the cursor on top of the file. 
# Read the file storing its content in a variable, put the cursor on top of the file, write the content, write the content.
######################################################33

with open("./files/data.txt", "a+") as myfile:
    myfile.seek(0)
    content = myfile.read()
    myfile.seek(0)
    myfile.write(content)
    myfile.write(content)
    
"""
