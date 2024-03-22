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
    #Create checking account object
    checking_account = Checking_Account(300)
    
    #Display initial balance of the checking account
    print('Initial checking account balance: £', checking_account.get_balance())
    
    #Deposit into savings_account
    checking_account.deposit(300)
    
    #Display new balance of account after deposit
    print('New balance with deposit: £', checking_account.get_balance())    
    
    #Withdraw from savings_account
    checking_account.withdraw(200)
    
    #Display final balance of account after withdrawal
    print('Final balance after withdrawal: £', checking_account.get_balance())   
    
    #Create savings_account object
    savings_account = Savings_Account(200)
    
    #Display current balance of the account
    print('Savings account balance: £', savings_account.get_balance())
    
    #Deposit into savings_account
    savings_account.deposit(300)
    
    #Display new balance of account after deposit
    print('New balance: £', savings_account.get_balance())    
    
    #Withdraw from savings_account
    savings_account.withdraw(450)
    
    #Display final balance of account after withdrawal
    print('Final balance: £', savings_account.get_balance())        
    
#Start program
main()
