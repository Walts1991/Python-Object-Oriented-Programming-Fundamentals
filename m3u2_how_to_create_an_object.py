class Employee:
    'base class for employees'

    def __init__(self):
        self.first_name = 'James'
        self.last_name = 'Bond'
        self.age = 42
        self.uid = '321'

def main():
    employee_01 = Employee() #case sensitive
    employee_02 = Employee()
    employee_03 = Employee()

main()
