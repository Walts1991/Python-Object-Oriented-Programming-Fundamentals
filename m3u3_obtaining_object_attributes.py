class Employee:
    'Base class for employee'

    def  __init__(self):
        self.first_name = 'James'
        self.last_name = 'Bond'
        self.age = 42
        self.uid = "321"

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_age(self):
        return self.age

    def get_uid(self):
        return self.uid

def main():
    employee_01 = Employee()

    #Access and print the first name.

    print('First name: ', employee_01.get_first_name())
    print('Last name: ', employee_01.get_last_name())
    print('Age: ', employee_01.get_age())
    print('User ID: ', employee_01.get_uid())

main()
