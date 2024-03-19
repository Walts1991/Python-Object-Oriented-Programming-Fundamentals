class Employee:
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
    employee = Employee()

#Begin our program
main()
