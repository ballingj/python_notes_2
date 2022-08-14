#####################################
#  file processing in python
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
# how to read file in python

myfile = open("fruits.txt")
# good idea to store the content in a variable because read operations leaves the cursor at the end of the file
content = myfile.read()

# by storing the content in a variable, we can print the content multiple times
print(content)

# close the file
myfile.close()

print(content)  # print the content even when the file is already closed

#############################
# opening files using 'with'
# advantage: closing the file is automatic after the intended block is done
# 3

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
# Read the file storing its content in a variable, put the cursor on top of the file, write the content
######################################################

with open("./files/data.txt", "a+") as myfile:
    myfile.seek(0)
    content = myfile.read()
    myfile.seek(0)
    myfile.write(content)
    myfile.write(content)
    
"""

"""
1) Basic write operation

file = open('file1.txt', 'w')
content = '''First Line
Second Line

Third Line'''
file.write(content)
file.close


2)  write file with "with" keyword
content = '''First Line
Second Line

Blank line then this Third Line
'''

with open('text_file1.txt', 'w') as file:
    file.write(content)

3) Read content of text file
with open('text_list_server.txt', 'r') as file:
    content = file.read()
    # one_line = file.readline()

print(content)
#print(one_line)

4) read and write multiple files
iterate over files in a directory and modify the texts

from pathlib import Path

files_dir = Path('my_dir')
for filepath in files_dir.iterdir():
    # print(filepath) # print the relative directory of file inside the Path('my_dir')

    # read the text content and add a new line
    with open(filepath, 'r') as file:
        content = file.read()
        new_content = content + "\n"

    # take the new content above and add another line then write
    with open(filepath, 'w') as file:
        newer_content = "Hello World\n"
        file.write(new_content + newer_content)


# 5) replace a word
from pathlib import Path

files_dir = Path('my_dir')
old_word = 'Earth'
new_word = 'World'

for filepath in files_dir.iterdir():
    with open(filepath, 'r') as file:
        content = file.read()
        new_content = content.replace(old_word, new_word)

    with open(filepath, 'w') as file:
        file.write(new_content)


# 6) Merge content of multiple text files
from pathlib import Path

files_dir = Path('my_dir')

merged = ''

# first read each file and concatenate each
for filepath in files_dir.iterdir():
    with open(filepath, 'r') as file:
        content = file.read()
    merged = merged + content + '\n'

# write the new merged content
with open('my_dir\merged.csv', 'w') as file:
    file.write(merged)

# 7) read list of servers
with open('text_list_server.txt') as file:
    servers = file.readlines()

print(servers)
# servers is a list -> ['omhqp1111\n', 'omhqp1112\n', 'omhqp1113\n', 'omhqp1114\n', 'omhqp1115']

for server in servers:
    # rstrip() eliminates the '\n' character at end of each line
    print(server.rstrip())

"""
