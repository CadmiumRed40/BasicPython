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