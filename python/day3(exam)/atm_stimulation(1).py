
def check_balance(balance):
    print(f"The balance in your account is: {balance}\n")
def withdraw_money(balance):
    w=float(input("The the amount you want to withdraw: "))
    if(w<=balance):
        print("successful withdraw of amount\n")
        balance-=w
    else:
        print("Sorry, your balance is too low for a withdrawal\n")
    return balance

def deposit_money(balance):
    d=float(input("Enter the amount you want to deposit: "))
    balance+=d
    print("Successful deposit\n")
    return balance

def exit():
    print("Thank you for using ATM\n")
def main():
    balance=0.0
    while True:
        print("\nPlease enter the number from below choices")
        print("Enter 1 for checking balance")
        print("Enter 2 for depositing money")
        print("Enter 3 for withdrawing money")
        print("Enter 4 for Exit")
        n=int(input("Enter the number:"))
        if(n<0 or n>4):
            print("Invalid input")
            return
        else:
            if(n==1):
                check_balance(balance)
            elif(n==2):
                balance=deposit_money(balance)
            elif(n==3):
                balance=withdraw_money(balance)
            elif(n==4):
                exit()
                break
        


main()
