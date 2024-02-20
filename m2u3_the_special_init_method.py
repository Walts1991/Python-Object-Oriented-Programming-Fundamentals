#Special method called init
#__init__ method responsibility is to initialize data attributes within the class
#Basic constructor

class Employee: #Base class for employee

    #This is our initializer method when a new object is created
    def __init__(self): #key word self assigns itself to a new object when created in a class
        #Declare some data attributes
        self.name = "Name"
