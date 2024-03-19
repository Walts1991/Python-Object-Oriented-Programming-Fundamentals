class BankAccount():
    def __init__(self, my_starting_balance):
        self.__balance = my_starting_balance   #Can only be accessed within class if __ is used

    def get_balance(self):
        return self.__balance

    def deposit(self, amount_to_deposit):
        self.__balance += amount_to_deposit

def main():
    #Create a new account
    account = BankAccount(600)

    #Display initial balance
    print('Starting Balance: £', account.get_balance())

    #Try to hack the balance
    account.deposit(500)
    #account.balance += 4000 #Error as cannot be accessed outside of class

    #Display balance
    print('Current Balance: £', account.get_balance())

#Start the program
main()
