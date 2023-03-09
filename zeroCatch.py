def div42by(divideBy):
    return 42 / divideBy
        except ZeroDivisionError: #2: this line of code helps to catch user inputs of 0
            print('Error: You tried to divide by zero')

print(div42by(2))
print(div42by(12))
print(div42by(0)) #1: computers have a hard time dividing by 0 and usually causes a bug
print(div42by(1))
