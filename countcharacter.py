message = "It was a a bright cold day in April and the clocks were striking thirteen."
count = {} # "r" : 12
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

