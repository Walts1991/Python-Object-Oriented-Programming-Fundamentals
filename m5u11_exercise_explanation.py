import m5u7_savings_account #import classes / modules
import m5u7_checking_account

def main():
    
    #Create a savings account and a checking account
    mySavingsAccount = m5u7_savings_account.Savings_Account(100)
    myCheckingAccount = m5u7_checking_account.Checking_Account(500)
    
    #Display the initial balance for both accounts
    print('Savings account balance: $', mySavingsAccount.get_balance())
    print('Checking account balance: $', myCheckingAccount.get_balance())
    print()
    print('Making a deposit into checking account for $75...')
    print()
    myCheckingAccount.deposit(75)
    print('New checking account balance: $', myCheckingAccount.get_balance())
    print()
    print('Making a deposit into savings account for $300...')
    print()
    mySavingsAccount.deposit(300)
    print('New savings account balance: $', mySavingsAccount.get_balance())

#Run program
main()