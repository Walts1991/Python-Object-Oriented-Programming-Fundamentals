class BankAccount: #Parent class
    #Base class for bank accounts
    
    #The __init__ method initialises the balance attribute with a starting balance
    def __init__(self,initial_balance):
        self.__balance = initial_balance
        
    #Deposits money into an account
    def deposit(self, amount):
        self.__balance += amount
        
    #Withdraws money from an account
    def withdraw(self, amount):
        if amount > self.__balance:
            print('Insufficient funds!\n')
        else:
            self.__balance -= amount
        
    def get_balance(self):
        return self.__balance
         
class CheckingAccount(BankAccount):
    #Child class from BankAccount- Inherits data attributes and methods from parent class
    def __init__(self, initial_balance):
        BankAccount.__init__(self, initial_balance)
        
    def transfer(self, account_obj, amount):
        if amount <= account_obj.get_balance():
            account_obj.withdraw(amount)
            self.deposit(amount)
            print('Transferred $',amount,'into your checking account.\n')
        else:
            print('Insufficient funds!\n')
                   
class SavingsAccount(BankAccount):
    #Child class from BankAccount- Inherits data attributes and methods from parent class
    def __init__(self, initial_balance):
        BankAccount.__init__(self, initial_balance)
        
    def transfer(self, account_obj, amount):
        if amount <= account_obj.get_balance():
            account_obj.withdraw(amount)
            self.deposit(amount)
            print('Transferred $',amount,'into your savings account.\n')
        else:
            print('Insufficient funds!\n')
