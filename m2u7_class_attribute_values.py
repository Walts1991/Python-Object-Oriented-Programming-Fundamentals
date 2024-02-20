class Employee:
    "Base class for our Employees"

    #Class attributes - simplest way to set up class attributes
    first_name = "James"
    last_name = "Bond"
    age = "42"
    userID = "321"

#main method
def main():
    print("First name: ",Employee.first_name)  # Accessing the class attribute directly
    print("Last name: ",Employee.last_name)
    print("Age: ",Employee.age)
    print("User ID: ",Employee.userID)

main()
