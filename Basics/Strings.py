#Strings.py

# Create a variable and assign it the string "Just do it!"

# Access the "!" from the variable by index and print() it

# Print the slice "do" from the variable

# Get and print the slice "it!" from the variable

# Print the slice "Just" from the variable

# Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".  
# Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.

myString = "Just do it!" #11 chars
print(myString[10:])
print(myString[5:7])
print(myString[8:])
print(myString[:4])

doIt = myString[5:]
dont = "Don't"
concatinated = dont + " " + doIt 
print(concatinated)

print("------------------------------")

boolValue = False
print(str(boolValue))

print("------------------------------")
print("abcdefghijklmn"[3:6])
print(len("abcdefghijklmn"[3:6]))

print("------------- String reverse -----------------")
input = input("Enter your input : ")
output = ""
for num in range(len(input) - 1, -1, -1) :
    output += input[num]
print("Reversed string: " + output)

print("------------- Word counter -----------------")
input = input("Enter your input : ")
myList = input.split()
print(myList)
print(len(myList))

str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."
 
 
# This function reduces the string to letters, numbers, spaces, hyphens, and apostrophes, and assigns that string to
# the variable spaces_and_letters so that the number of words in it can by found by counting spaces between words.
def word_counter(words):
    spaces_and_letters = ""
    word_count = 1
    for i in words:
        if i.isalnum() or i.isspace() or i == "-" or i == "'":
            spaces_and_letters += i
    for j in spaces_and_letters:
        if j == " ":
            word_count += 1
    return word_count
 
 
print(word_counter(str_1))
print(word_counter(str_2))
print(word_counter(str_3))

