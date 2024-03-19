class Employee():

    def __init__(self, myFirstName, myLastName, myUID):
        self.first_name = myFirstName
        self.last_name = myLastName
        self.user_id = myUID

    def show_employee_details(self):
        print('First Name:', self.first_name)
        print('Last Name:', self.last_name)
        print('User ID:', self.user_id)

def main():
    #Create new object
    employee01 = Employee('James','Bond','123')
    employee02 = Employee('John','Smith','456')

    #Display employee details
    employee01.show_employee_details()
    employee02.show_employee_details()

#Start the program
main()
