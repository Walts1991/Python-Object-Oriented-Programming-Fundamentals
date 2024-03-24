class BankAccount: #Parent Class
    #Base class for bank accounts

    #The __init__ method initalises the balance attribute with a starting balance
    def __init__(self,starting_balance):
        self.__balance = starting_balance
        
    #Deposits money into an account        
    def deposit(self, amount):
        self.__balance += amount
    
    #Withdraws money from an account
    def withdraw(self, amount):
        if amount > self.__balance:
            print('Insufficient funds!')
        else:
            self.__balance -= amount
            
    #Transfers money from savings account
    def transferfrom(self, amount):
        self.__balance -= amount
        
    #Transfers money to savings account
    def transferto(self, amount):
        self.__balance += amount   
          
    #Retrieves the current balance of the given account
    def get_balance(self):
        return self.__balance
    
            
class Savings_Account(BankAccount): #Child class of BankAccount

    #The __init__ method initialises the BankAccount balance data attribute with the initial_balance argument
    def __init__(self, initial_balance):
        #Call the __init__ method from the BankAccount class and initialise the initial_balance data attribute
        BankAccount.__init__(self, initial_balance)
