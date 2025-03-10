# CarRentalSystem.py

# write a program to provide layers of abstraction for a car rental system.
# Program should perform the following:
# 1. Hatchback, Sedan, SUV should be type of cars that are being provided for rent
# 2. Cost per day: Hatchback - $30 Sedan - $50 SUV - $100
# 3. Give a prompt to the customer asking him the type of car and the number of days he would like to borrow 
#     and provide the fare details to the user.

class Car:
    def __init__(self):
        # A dictionary to map the type of car and price per day
        self.carFare = {'Hatchback': 30, 'Sedan': 50, 'SUV': 100}

    def displayFareDetails(self):
        print("Cost per day: ")
        print("Hatchback: $",self.carFare['Hatchback'])
        print("Sedan: $", self.carFare['Sedan'])
        print("SUV: $", self.carFare['SUV'])

    def calculateFare(self, typeOfCar, numberOfDays):
        # Calculate the fare depending upon the type of car and number of days as requested by the user
        return self.carFare[typeOfCar] * numberOfDays


car = Car()
while True:
    print("Enter 1 to display the fare details")
    print("Enter 2 to rent a car")
    print("Enter 3 to exit")
    userChoice = (int(input()))
    if userChoice is 1:
        car.displayFareDetails()
    elif userChoice is 2:
        print("Enter the type of car you would like to borrow")
        typeOfCar = input()
        print("Enter the number of days you would like to borrow the car")
        numberOfDays = int(input())
        fare = car.calculateFare(typeOfCar, numberOfDays)
        print("Total payable amount: $",fare)
        print("Thank you!")
    elif userChoice is 3:
        quit()