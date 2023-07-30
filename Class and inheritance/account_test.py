
import bankaccount
import datetime, time, calendar
def main():
    # Get the starting balance.
    name = input("Enter bank name:")
    acc_num = input("Enter 8 digits bank account num:")
    start_bal = float(input('Enter your sarting balance:'))

    # creat a bnak account objects
    checking = bankaccount.BankAccount(name,acc_num, start_bal)

    print()

    # Deposit the user's paycheck
    pay = float(input('How much were  you paid this week?'))
    print("I will deposite that into your account.")
    checking.deposite(pay)

    # Display the balance
    print(f'Your account balance is ${checking.get_balance():,.2f}.')

    # get the amount to withdraw
    cash = float(input('How much would you like to withdraw?'))
    print('I will withdraw that from your account.')
    curr = checking.withdraw(cash)

    print(f'Your account balance is ${checking.get_balance():,.2f}.')
    print()


    print("Bank Account Information")
    print('-------------------------')
    print(f'BankName: {checking.get_name()}')
    print(f'Bank Account Number: {checking.get_account_num()}')
    print(f'Bank Balance:  ${checking.get_balance():,.2f}.')

def saving_account():

    name1 = input("Enter bank name:")
    acc_num1 = input("Enter 8 digits bank account num:")
    start_bal1 = float(input('Enter your sarting balance:'))
    int_rate = float(input("Current interest rate?"))

    try:
        number = int(acc_num1)
        return number
    except ValueError:
        print("Error in number format:", acc_num1)
        

    sv = bankaccount.SavingAccount(name1,acc_num1,start_bal1, int_rate);

    savacc = float(input("How much would you like to deposite on saving account?"))
    print('I will senf to saving account')
    balance1 = start_bal - savacc
    sv.deposite(savacc)
    

    print('\n')
    print('Saving account')
    print('---------------')
   

# Call the main function

if __name__ == '__main__':
    #today  = datetime.date.today()
    #print(today)

    format = "%a %b %d %H:%M:%S %Y"

    today = datetime.datetime.today()

    s = today.strftime(format)
    print('time:', s)
    main()
    saving_account()
