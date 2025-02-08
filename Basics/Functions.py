# Functions.py

def name_printer(name):
    print(name)

name = input("Type your name: ")
name_printer(name)

# --------------------------

def print_globe():
    print(globe_var)

globe_var = "Hi"
print_globe()

# --------------------------

# To assign a new value to global variable within a function

def assign():
    global fruit
    fruit = "pear"
    return fruit

fruit = "apple"
assign()
print(fruit)