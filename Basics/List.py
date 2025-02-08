# List.py

# Create a variable called arctic_animals and assign it the list ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]

# Use del to remove "tiger" from the list assigned to arctic_animals.

# Use the .remove() method to remove the string "elephant" from the list assigned to arctic_animals.

# Use the .append() method to add the string "arctic fox" to the list arctic_animals.

# Use .insert() to insert the string "snowy owl" between the strings "polar bear" and "walrus" inside of arctic_animals.

# Use the .sort() method to rearrange the strings in arctic_animals into alphabetical order.

# Use print() to display the list assigned to arctic_animals

# Use .index() to get the index number of "reindeer" from arctic_animals then print it.

# Use .pop() to get the last item from the list arctic_animals then print it.

arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
indexOfTiger = arctic_animals.index('tiger')
del arctic_animals[indexOfTiger]
print(arctic_animals)
arctic_animals.remove("elephant")
print(arctic_animals)
arctic_animals.append("arctic fox")
print(arctic_animals)
indexOfPB = arctic_animals.index('polar bear')
arctic_animals.insert(indexOfPB + 1, "snowy owl")
print(arctic_animals)
arctic_animals.sort()
print(arctic_animals)
print(arctic_animals.index("reindeer"))
print(arctic_animals.pop())
