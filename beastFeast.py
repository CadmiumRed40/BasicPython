Beast = str(input("What beast is coming to the feast? ")).lower()
Dish = str(input ("What dish do they bring? ")).lower()

if Beast[0] == Dish[0]:
    print("The " + Beast + " can bring their " + Dish)
else:
    print("The " + Beast + " cannot bring their " + Dish +" because the first letter of their names do not match!")