class BankAccount:
    #Parent class
    def __init__(self,initial_balance):
        self.__balance = initial_balance
        
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        self.__balance -= amount
        
class Savings_Account(BankAccount):
    #Child class from BankAccount- Inherits data attributes and methods from parent class
    def __init__(self, initial_balance):
        BankAccount.__init__(self, initial_balance)
        
def main():
    savings_account = Savings_Account(200)
    
#Start program
main()