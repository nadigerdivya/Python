# FizzBuzz.py

def FizzBuzz() : 
    rangeValue = range(1, 20)
    for num in rangeValue : 
        if num % 3 == 0 and num % 5 == 0:
            print('Fizzbuzz')
        elif num % 3 == 0 :
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else :
            print(num)

FizzBuzz()
