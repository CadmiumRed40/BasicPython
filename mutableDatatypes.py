def eggs(cheese)
    cheese.append('Hello')#calls append method

spam = [1, 2, 3] #mutable datatype
eggs(spam)#attaching cheese to the list 
print(spam)#will pull up the list and hello instead of just the list.
