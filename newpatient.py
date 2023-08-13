name = input("Please enter your name? ")
age = input("Hello, " + name + " enter your birth year: ")
final_age = 2023 - int(age)
new_patient = input("Are you a new patient? ")

if new_patient == "yes":
    print("Welcome to PyHospital" + name + "!")
else:
    print("Sorry to see you here again. How can I help you today" + name +"?")

