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
        
class Checking_Account(BankAccount):
    #Child class from BankAccount- Inherits data attributes and methods from parent class
    def __init__(self, initial_balance):
        BankAccount.__init__(self, initial_balance)
                   
class Savings_Account(BankAccount):
    #Child class from BankAccount- Inherits data attributes and methods from parent class
    def __init__(self, initial_balance):
        BankAccount.__init__(self, initial_balance)
        
def main():
    #Create savings account object
    savings_account = Savings_Account(100)
    #Create checking account object
    checking_account = Checking_Account(500)
    
    #Display initial balance of the checking account
    print('Savings account balance: $', savings_account.get_balance())    
    
    #Display initial balance of the checking account
    print('Checking account balance: $', checking_account.get_balance())
    print()
    
    #Deposit into checking account
    checking_account.deposit(75)
    print('Making deposit into checking account for $75...')
    print()
    
    #Display new balance of account after deposit
    print('New checking account balance: $', checking_account.get_balance())   
    print() 
    
    #Deposit into savings_account
    savings_account.deposit(300)
    print('Making deposit into savings account for $300...')
    print()
    
    #Display new balance of account after deposit
    print('New savings account balance: $', savings_account.get_balance())
    
#Start program
main()