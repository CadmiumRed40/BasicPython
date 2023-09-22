def isPhoneNumber(text): # Checking to see if an entered value is a phone number.
    if len(text) != 12:
        return False # not phone number sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first 3 digits
        if text[7] != '-':
            return False # missing second dash
        for i in range (8, 12):
            if not text[i].isdecimal():
                return False # missing last 4 digits
    return True
        
#test

isPhoneNumber('Hello')
isPhoneNumber('914-245-2345')

message = 'Call me at 402-263-2344, or at 246-342-1745 to reach my personal line'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
if not foundNumber:
    print('Could not find a phone number')