# GuessingGame.py

# Call the Guessing function which checks the secret number with the input given. 

# There should be 3 chances to guess the number.

def check_value(input) :
    sec_number = 9
    if input == sec_number :
        return True
    else :
        return False

def Guess_the_Number() :
    attempts = 0
    guessed = False
    while attempts < 3 :
        value = int(input('Guess : '))
        guessed = check_value(value)
        if guessed == True :
            break
        attempts += 1

    if guessed == True :
        print("Hurray!! Your guessing is correct")
    else :
        print("Sorry!! You failed")

print(Guess_the_Number())