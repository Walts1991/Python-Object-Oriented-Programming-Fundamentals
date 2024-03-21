class Employees:
    "Base class for employees"

    #The init method will initialise the object attributes with default values when new object is created

    def __init__(self):
        self.first_name = "n/a"
        self.last_name =  "n/a"
        self.uid = "n/a"
        self.position_type = "n/a"

    #Getter methods
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_uid(self):
        return self.uid
 
    def get_position_type(self):
        return self.position_type

    #Setter methods
    def set_first_name(self, xFirstName):
        self.first_name = xFirstName

    def set_last_name(self, xLastName):
        self.last_name = xLastName

    def set_uid(self, xUID):
        self.uid = xUID

    def set_position_type(self, xPositionType):
        self.position_type = xPositionType

def main():
    employee_01 = Employees()

    print('First name:',employee_01.get_first_name())
    print('Last name:',employee_01.get_last_name())
    print('User ID:',employee_01.get_uid())
    print("Position Type:",employee_01.get_position_type())
    print()

    #Modify object attribute values
    employee_01.set_first_name("James")
    employee_01.set_last_name("Bond")
    employee_01.set_uid("007")
    employee_01.set_position_type("Agent")

    print("*** New changes ***\n")
    print('First name:',employee_01.get_first_name())
    print('Last name:',employee_01.get_last_name())
    print('User ID:',employee_01.get_uid())
    print("Position Type:",employee_01.get_position_type())

#Begin our program
main()
