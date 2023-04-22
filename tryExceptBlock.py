print('How many cats do you have?')
numCats = input()#asking for user input to define our variable for cats.
try: #similar to a try catch statement in JS
    if int(numCats) >= 4: #if statement checks if the number of cats is greater than 4
        print('That is alot of cats!')
    else: #if less than 4 it prints out this message
        print('That is not that many cats.')
except ValueError: #check if the user input something that is not a number
    print('You did not enter a number.') 
