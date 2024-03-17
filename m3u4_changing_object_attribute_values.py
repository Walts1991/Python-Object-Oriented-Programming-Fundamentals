class Employees:
    "This is the base class for employees"
    
    #Default constructor when new objects are created
    
    def __init__(self):
        self.first_name = "n/a"
        self.last_name = "n/a"
        self.uid = "n/a"
        
def main():
    employee_01 = Employees()
    print("First name: ",employee_01.first_name)
    print("Last name: ",employee_01.last_name)
    print("User ID: ",employee_01.uid)
    
    print()
    
    #Let's modify these object attribute values.

    employee_01.first_name = "Bobby"
    employee_01.last_name = "Jones"
    employee_01.uid = "522"
     
     #Print the new assigned values
    print("New values")
    print()
    print("First name: ",employee_01.first_name)
    print("Last name: ",employee_01.last_name)
    print("User ID: ",employee_01.uid)
       
#Start our program    
main()
    