#method is a function within a class that performs a task on the attributes

class Emplopyee:
    #this is the base Employee class
    def __init__(self):
        self.firstName = "N/A"
        self.lastName = "N/A"
        self.userID = "N/A"

#define a method like a function - "def [name](self)
    def operation01(self): #self is mandatory for method
        print("This is an employee")
    def operation02(self): #self is mandatory for method
        print("My user ID is "+str(self.userID))
    def operation03(self): #self is mandatory for method
        full_name = self.firstName + " " + self.lastName
        print(full_name)

#examples above within the def operations are AI generated
