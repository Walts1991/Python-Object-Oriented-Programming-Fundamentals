#How to look at public visibility of object attribute values outside of class
#Disadvantages / Dangers allowing others to update class attribute values outside of the class

class BankAccount():

    def __init__(self, my_initial_balance):
        self.balance = my_initial_balance

    def get_balance(self):
        return self.balance

def main():

    #Create new bank account
    account = BankAccount(500)

    #Display current balance
    print('Current balance: £', account.get_balance())

    account.balance += 8000000
    print('New balance: £', account.get_balance())

#Begin our program
main()
