import re

# finding a phone number in the format 415-555-1234
# much simplified with the use of regex


message = 'Call me at 415-555-1010 tomorrow, or at 415-555-1919'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)   # create a match object (mo)
print(mo.group())

# grab all occurence of a match: result is a list
mo_all = phoneNumRegex.findall(message)
print(mo_all)

for _ in mo_all:
    print(_)


# grouping results with a ()
message1 = 'Call me at 501-555-2435 or 501-555-3456'
phoneNumRegex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1 = phoneNumRegex1.search(message1)  
print(mo1.group(1))  # mo1.group(1) represents the first group
print(mo1.group(2))  # mo1.group(2) represents the second group


# what if you need to find an actual parentesis ()? 
message2 = 'Call me at (501) 555-2435 or (501) 555-3456'
phoneNumRegex2 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo2 = phoneNumRegex2.search(message2)
print(mo2.group())  # there is no group 1 or 2 in this mo2 object


# Finding a words
message3 = 'Batmobile lost a wheel'
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = batRegex.search(message3)
print(mo3.group(0))  # 0 or blank in group() returns the found word
print(mo3.group(1))  # if you want to see what word from the piped characters was found
