#How to create project example:

#GW solution

class Employee:

    firstName = "James"
    lastName = "Bond"
    age = 42

def main():
    print("************ Welcome to the Employee Database ************")
    print("First name: ",Employee.firstName)
    print("Last name: ",Employee.lastName)
    print("Age: ",Employee.age)
    print()

main()

#Actual solution

class Person:
    "Base class of a person"

    #Class Attributes:
    first_name = "James"
    last_name = "Bond"
    age = 42

def main():
    #Print the title of the program.
    print("\t************ Welcome to the Employee Database ************") #\t = tab
    print()

    #Print the class attribute values.
    print("First name: ",Person.first_name)
    print("Last name: ",Person.last_name)
    print("Age: ",Person.age)

#Call the main method to start the program
main()
