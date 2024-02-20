#class variables are defined names which hold values which can be shared across a class

class Employee:

    #Declare class variables at the top of the class
    employeeCount = 0
    payRate = 10


    def __init__(self):
        self.firstName = "N/A"
        self.lastName = "N/A"
        self.userID = "N/A"

print("Employee count: ",Employee.employeeCount) #[class].[classvariable]
print("Employee pay rate: ",Employee.payRate)
