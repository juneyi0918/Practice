#learn how to use function

def open_account():
    print("New account is created")

def deposit(balance, money):
    print("Deposit is completed. New Balance is : ${0}".format(balance+money))
    return balance + money

def withdraw(balance, money):
    if balance>=money:
        print("Withdraw ${0} is sucessful. New Balance is : ${1}".format(money,balance-money))
        return balance - money  
    else:
        print ("Withdraw amount is bigger than your Balance")
        return balance

def withdraw_night(balance, money):
    commission = 100 
    print ("withdraw $ {0} at night is sucessful. ${1} is commision. New Balance is ${2} ".format(money,commission,balance-commission-money))

    return commission, balance - money - commission


balance = 0
balance = deposit(balance,1000)
# balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance,900)

print(balance)