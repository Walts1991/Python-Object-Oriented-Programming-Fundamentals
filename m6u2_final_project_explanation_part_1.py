import m6u2_account_type

#Make method
def main():
    
    #Setup a checking and savings account
    my_savings_account = m6u2_account_type.SavingsAccount(100)
    my_checking_account = m6u2_account_type.CheckingAccount(500)
    
    #Display the current balance for both accounts
    print('Savings account balance: $', my_savings_account.get_balance())
    print('Checking account balance: $', my_checking_account.get_balance(),'\n')

    #Transfer money from checking account to savings account
    
    my_savings_account.transfer(my_checking_account,100)

    #Display new savings account and checking account balance
    print('Savings account balance: $', my_savings_account.get_balance())
    print('Checking account balance: $', my_checking_account.get_balance())    
    
#Run the program
main()