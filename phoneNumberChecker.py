def isPhoneNumber(text):
    if len(text) != 12: #checking length
        return False #not phone number sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False #missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False #no first 3 digits
        if text[7] != '-':
            return False #missing second dash
        for i in range(8,12):
            return False #missing last 4 digits
        return True