class BankAccount:

    #The __init_ method initialises the data members with the arguments:
    #firstName, lastName, account_number and xBalance

    def __init__(self,firstName,lastName,account_number,xBalance):
        self.__first_name = firstName
        self.__last_name = lastName
        self.__account_num = account_number
        self.__balance = xBalance

    #Get account details

    def get_account_details(self):
        print('First Name:', self.__first_name)
        print('Last Name:', self.__last_name)
        print('Account Number:', self.__account_num)
        print('Balance: £', self.__balance, sep='')
        print()

def main():
    #Create three new accounts
    account_01 = BankAccount('Victor','Davis','5632',300)
    account_02 = BankAccount('Jason','Wilson','7852',600)
    account_03 = BankAccount('Scott','James','4112',200)

    #Display the account details for each account
    account_01.get_account_details()
    account_02.get_account_details()
    account_03.get_account_details()

#Run program
main()
