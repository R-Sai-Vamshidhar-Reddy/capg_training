class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amt):
        if(amt<=self.balance):
            print("Withdrawal is successful")
        else:
            print("Withdrawal is failed due to insuffient balance")

    def deposit(self,amt):
        if(amt<0):
            print("Invalid amount, amount should be greater than 0")
        else:
            self.balance+=amt
            print("Successful deposit")

obj=BankAccount(0)
while True:
    n=int(input("Enter\n1.deposit\n2.withdraw\n3.exit\n"))
    if(n==1):
        m=float(input("Enter depositing amount: "))
        obj.deposit(m)
    elif(n==2):
        m=float(input("Enter withdrawal amount: "))
        obj.withdraw(m)
    elif(n==3):
        break