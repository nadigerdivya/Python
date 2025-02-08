# Factorial.py

def factorial(num) :
   rangeValue = range(num, 1, -1) # starts with num, ends at 2, decrements by 1
   res = 1
   for val in rangeValue :
       res *= val
   return res

input = int(input('Enter the number : '))
print(factorial(input))