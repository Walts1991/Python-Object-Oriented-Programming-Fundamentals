class Employees:
    "Base class for employees"

    def __init__(self):
        self.first_name = "James"
        self.last_name =  "Bond"
        self.uid = "123"

    #Getter methods
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_uid(self):
        return self.uid

    #Setter methods 
    def set_first_name(self, xFirstName):
        self.first_name = xFirstName

    def set_last_name(self, xLastName):
        self.last_name = xLastName

    def set_uid(self, xUID):
        self.uid = xUID

def main():
    employee = Employees()
    print('First name: ',employee.get_first_name())
    print('Last name: ',employee.get_last_name())
    print('User ID: ',employee.get_uid())
    print()

    #Modify object attribute values
    employee.set_first_name("John")
    employee.set_last_name("Smith")
    employee.set_uid("321")

    print("New values")
    print()
    print('First name: ',employee.get_first_name())
    print('Last name: ',employee.get_last_name())
    print('User ID: ',employee.get_uid())

#Begin our program
main()
