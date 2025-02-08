# Dictionary.py

# create a variable and assign it the following dictionary:

# {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}
# make the dictionary span multiple lines so that the line the dictionary starts on is not too long.

# print the length of the dictionary.

# use the .keys() method and a for loop to get and print all of the keys from the dictionary on separate lines.

# print all of the values from the dictionary using the .values() method.

# use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary.

# use the .get() method to check the dictionary for the key

# "Promise of the Real"
# and create a message that will print if the key is not found in the dictionary.

famous_songs = {"Queen": "Bohemian Rhapsody",
                "Bee Gees": "Stayin' Alive",
                "U2": "One",
                "Michael Jackson": "Billie Jean",
                "The Beatles": "Hey Jude",
                "Bob Dylan": "Like A Rolling Stone"}  # 1 and 2
print(len(famous_songs))  # 3
for key in famous_songs.keys():  # 4
    print(key)
print(famous_songs.values())  # 5
for key, value in famous_songs.items():  # 6
    print(key, value)
print(famous_songs.get("Promise of the Real", "That is not a key that appears in the dictionary."))  # 7

print("--------------------------------")

# use .fromkeys() to create a dictionary that has the consonants from the alphabet as its keys and 
# the string "consonant" as the value for each of those keys.  Only use lower case letters for the consonants.  
# "y" counts as a consonant for this exercise.  Use a for loop and the .items() method to print each of those key: 
# value pairs on a different line.  For example, the first 3 lines in the output should be the following:

# b consonant

# c consonant

# d consonant

# paste this dictionary into your .py file then pop and print "Big Mac" from it

# fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
# use .popitem() to remove the last key: value pair from the dictionary assigned to fast_food_items then print new 
# fast_food_items dictionary.


for key, value in {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant").items():
    print(key, value)
 
fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
print(fast_food_items.pop("McDonald's"))
 
fast_food_items.popitem()
print(fast_food_items)
