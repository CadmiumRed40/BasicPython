guess = input("How hot/cold do you think it is? ")

temp = int(guess)

if temp > 60:
    print("man its kinda warm")
elif temp < 30:
    print("wow its cold!")
elif temp == 40:
    print("Nobody cares about a 40 degree day!")
