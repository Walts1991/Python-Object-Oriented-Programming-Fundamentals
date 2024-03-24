import m5u7_savings_account #import classes / modules
import m5u7_checking_account

def main():
    
    #Create a savings account and checking account with initial balances
    mySavingsAccount = m5u7_savings_account.Savings_Account(100)
    myCheckingAccount = m5u7_checking_account.Checking_Account(500)
    
    #Display the inital balance for both accounts
    print("Savings account balance: £", mySavingsAccount.get_balance())
    print("Checking account balance: £", myCheckingAccount.get_balance())

#Start the program
main()