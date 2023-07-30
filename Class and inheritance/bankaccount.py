class BankAccount:

    # the __init method accepts an argument for
    # the acount's balance. it is asigned to the __balance attribute

    def __init__(self, name, account_num, bal):

        self.__name = name
        self.__account_num = account_num
        self.__balance = bal
        
    # The following methods are mutators for the data attribute

    def set__name(self, name):
        self.__name = name

    def set_account_num(self, account_num):
        self.__account_num = account_num

    def set_balance(self, bal):
        self.__balance = bal

    # Accessor methods the get_balance method return the account balance

    def get_name(self):
        return self.__name

    def get_account_num(self):
        return self.__account_num

    def get_balance(self):
        return self.__balance

    # methods 
    def deposite(self,amount):
        self.__balance += amount
        


    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds')
               

    def __str__(self):
        return f'The balance is ${self.__balance:,.2f}'



class SavingAccount(BankAccount):
    # The __init __ methods accepts arguments for the
    # account number, interest rate, and balance

    def __init__(self, name, account_num, bal, int_rate):
        # Call the supercalss __init__ method
        BankAccount.__init__(self, name,account_num,bal)

        # Intialize the __int_rate__ attribute
        self.__interest_rate = int_rate
        #self.__date = mat_date


    # the following methods are mutores for the data attribute

    def set_interest_rate(self, int_rate):
        self.__interest_rate = int_rate

    """
    def set_date(self,mat_date):
        self.__date = mat_date
    """

    # The following methods are accessors for the data attribute

    def get_interest_rate(self):
        return self.__interest_rate
    """
    def get_date(self):
        return self.__date
    """
     
        
    
    
