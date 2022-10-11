# finding a phone number in the format 415-555-1234
# without using the regex


def isPhoneNumber(text):  # 415-555-
    if len(text) != 12:
        return False  # not a phone number sized
    for i in range(0, 3):  # first three char
        if not text[i].isdecimal():
            return False  # no area code
    if text[3] != '-':
        return False  #missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # no first three digits
    if text[7] != '-':
        return False  # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # missing last 4 digits
    return True

message = 'Call me at 415-555-1010 tomorrow, or at 415-555-1919'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')
