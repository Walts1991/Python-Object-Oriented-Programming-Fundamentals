class BankAccount:
    
    def __init__(self, myBalance):
        self.__balance = myBalance
        
    def get_balance(self):
        print('Call the get_balance method from the "parent" class')
        
class CheckingAccount(BankAccount):
    
    def __init__(self,myBalance):
        BankAccount.__init__(self, myBalance)
        
    def get_balance(self):
        print('Call the get_balance method from the "child" class')
        
    def get_balance2(self): #Call get_balance from the parent class
        BankAccount.get_balance(self)

def main():
    
    account = CheckingAccount(50)
    account.get_balance()
    account.get_balance2()

#Call the main function to start the program
main()