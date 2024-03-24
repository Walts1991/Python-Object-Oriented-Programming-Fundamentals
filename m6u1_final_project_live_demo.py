import m6u1_savings_account #import classes / modules
import m6u1_checking_account

def main():
    
    #Create a savings account and a checking account
    mySavingsAccount = m6u1_savings_account.Savings_Account(100)
    myCheckingAccount = m6u1_checking_account.Checking_Account(500)
    
    print("Savings account balance: $", mySavingsAccount.get_balance())
    print("Checking account balance: $", myCheckingAccount.get_balance())
    print()
    myCheckingAccount.transferfrom(100)
    mySavingsAccount.transferto(100)
    print("Transferred $100 into your savings account.")
    print()
    print("Savings account balance: $", mySavingsAccount.get_balance())
    print("Checking account balance: $", myCheckingAccount.get_balance())
    
#Run the program
main()