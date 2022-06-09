"""
list comprehension is an alternate way to iterate over a list:
instead of going through for loop, you can use a list iterator
"""

# some data are stored in a format designed to save space.  For example, the data below are temperature in celsius
# 221 is actually 22.1 and so forth.  Storing the data without the decimal point saves data storage space
# Task: convert the list back to the actual temperature in celsius

temps = [221, 234, 340, 230]

# old for loop way
new_temps1 = []
for temp in temps:
    new_temps1.append(temp/10)

print(new_temps1)

# this is list comprehension
##################################################
new_temps2 = [temp / 10 for temp in temps]

print(new_temps2)

# list comprehension with if statement
########################################################
# we got some invalid data in the list... '-9999' is invalid; let's exclude it
temps1 = [221, 234, 340, 230, -9999]
new_temps3 = [temp / 10 for temp in temps1 if temp != -9999]
print(new_temps3)

## define a function that takes as a parameter a list that contains both integers and strings and return the list containing only the integers.
#  my solution:
# def foo(list_data):
#     new_list = []
#     [new_list.append(i) for i in list_data if isinstance(i, int)]
#     return new_list

# new_list = foo([99, 'no data', 95, 94, 'no data'])
# print(new_list)

# ardit's solution:
def foo1(lst):
    return [i for i in lst if isinstance(i, int)]


## define a function that takes a parameter list of numbers and return the list containing only numbers greater than zero
# my solution
def foo2(list_data):
    return [i for i in list_data if i > 0]

new_list = foo2([-5, 3, -1, 101])
print(new_list)


# list comprehension with if-else statement
# the order of for loop changes -- goes to the end
# if -9999 then value replaced with "0"
# #######################################################
temps2 = [221, 234, 340, 230, -9999]
new_temps4 = [temp / 10 if temp != -9999 else 0 for temp in temps2]
print(new_temps4)

# define a function that takes as a parameter a list that contains both integers and strings and return the list replacing alpha with 0.
#  my solution:
def foo3(lst):
    return [i if isinstance(i, int) else 0 for i in lst]

new_list2 = foo3([99, 'no data', 95, 94, 'no data'])
print(new_list2)

# define a function that takes as a parameter a list that contains decimal numbers as string and returns the sum of those numbers.
#  my solution:
def foo4(lst):
    return sum([float(i) if isinstance(i, str) else 0 for i in lst])
    
new_list3 = foo4(['1.2', '2.6', '3.3'])
print(new_list3)

#Ardit's solution
# def foo(lst):
#    return sum([float(i) for i in lst])


"""
Cheatsheet: List Comprehensions
In this section, you learned that:

A list comprehension is an expression that creates a list by iterating over another container.

A basic list comprehension:

[i*2 for i in [1, 5, 10]]
Output: [2, 10, 20]

List comprehension with if condition:

[i*2 for i in [1, -2, 10] if i>0]
Output: [2, 20]

List comprehension with an if and else condition:

[i*2 if i>0 else 0 for i in [1, -2, 10]]
Output: [2, 0, 20]
"""
