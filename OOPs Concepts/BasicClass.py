# BasicClass.py

#class creation 
class Employee :
    # constructor methood
    def __init__(self, name = "Divya", designation = 'Software Developer') :
        self.name = name
        self.designation = designation

    #static methods
    @staticmethod
    def myStaticMethod() :
        print('A init menthod is called')

    #instance method
    def getEmployeeDetails(self) :
        print('Name :' + self.name)
        print('Designation: ' + self.designation)


#Accessing class / instantiating class
employee1 = Employee()
employee1.getEmployeeDetails()

employee2 = Employee("Divyashree", "Frontend Engineer")
employee2.getEmployeeDetails()