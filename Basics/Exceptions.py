# Exceptions.py

def getAge() :
    try :
        print()
        age = int(input("Enter age :: "))
        income = 20000
        risk = income / age
        print(age)
        print(risk)
    except ZeroDivisionError:
        print("Error :: Age cannot be zero")
    except ValueError:
        print("Error :: Invalid value")

getAge()