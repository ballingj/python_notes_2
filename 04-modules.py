"""
Cheatsheet: Imported Modules
In this section, you learned that:

Builtin objects are all objects that are written inside the Python interpreter in C language.

Builtin modules contain builtins objects.

Some builtin objects are not immediately available in the global namespace. They are parts of a builtin module. To use those objects the module needs to be imported first. E.g.:

import time
time.sleep(5)
A list of all builtin modules can be printed out with:

import sys
sys.builtin_module_names
Standard libraries is a jargon that includes both builtin modules written in C and also modules written in Python.

Standard libraries written in Python reside in the Python installation directory as .py files. You can find their directory path with sys.prefix.

Packages are a collection of .py modules.

Third-party libraries are packages or modules written by third-party persons (not the Python core development team).

Third-party libraries can be installed from the terminal/command line:

Windows:

pip install pandas or use python -m pip install pandas if that doesn't work.

Mac and Linux:

pip3 install pandas or use python3 -m pip install pandas if that doesn't work.

###############################################33
# search str methods with dir
dir(str)

# search builtin functions with dir(__builtins__)
dir(__builtins__)

# search for built in modules
import sys
sys.builtin_module_names

# we'll find time as one of the builtin modules
import time
# find what modules are under time
dir(time)
# find sleep
time.sleep(10)  # sleep for 10 seconds
"""

import time

# while True:
#     with open("./files/vegetables.txt") as myfile:
#         print(myfile.read())
#         time.sleep(10)


"""
# Search python modules
in python session:
sys.prefix  # open the directory to find the built in python modules
# output:  'C:\\Users\\Jeff\\AppData\\Local\\Programs\\Python\\Python39'

# we found os.py as one of the modules
import os
dir(os)
 # use some functions
 os.mkdir(dirname)
 os.path.exists(filename)


"""
import os
while True:
    if os.path.exists("./files/vegetables.txt"):
        with open("./files/vegetables.txt") as myfile:
            print(myfile.read())
    else:
        print("file does not exist.")
    time.sleep(10)

