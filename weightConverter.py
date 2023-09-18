weight = int(input("How much do you weight? "))

print(weight)

conversion = input("In (K)bs or (L)bs? ").lower()

if conversion == 'k':
    lbsWeight = float(weight * 2.5)
    print("You weight ", lbsWeight, " lbs!")
elif conversion == 'l':
    kiloWeight = float(weight / 2.5)
    print("You weight " , kiloWeight, " kilos!")