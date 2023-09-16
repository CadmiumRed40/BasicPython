def hot_singles(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    result = set1.symmetric_difference(set2)

    return list(result)

#The main takaway here is to take the arguments and converts arrays to remove 
# duplicates and then using the built in function "symmetric difference", you 
# can pull the difference between arrays and set them as the result variable.