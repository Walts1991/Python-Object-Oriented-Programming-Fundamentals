#Inheritance is a class that inherits its class feature such as data attributes and methods
#Useful so we don't have to rewrite code
#Can write new attributrs for the inherited class
#Parent class is the more general class
#Child class inherits features from parent class and is more specific

class BankAccount:
    #Parent class
    def __init__(self, initial_balance):
        self.__balance = initial_balance
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if amount > self.__balance:
            print('You do not have sufficient funds to withdraw the chosen amount')
        else:
            self.__balance -= amount
        
    def get_balance(self):
        return self.__balance
    
def main():
    account = BankAccount(100)
    print('Account balance: £', account.get_balance())
    
    #Deposit £300 into account
    account.deposit(150)
    print('New balance after deposit: £', account.get_balance())
    
    #Deposit £300 into account
    account.withdraw(220)
    print('Final balance after withdrawal: £', account.get_balance())
    
#Start the program
main()
