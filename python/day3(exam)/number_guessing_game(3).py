import random
def main():
    print("The system will generate a number and you have to guess the number")
    print("And you have only ten chances")
    chances=10
    n=random.randrange(100)
    attempts=0
    while(attempts<=chances):
        attempts+=1
        m=int(input("Enter the guess number: "))
        if(n==m):
            print("Hurray!! You have guessed it correct")
            break
        elif(attempts>=chances and n!=m):
            print("OOPS your chances are finished, better luck next time")
        elif(m<n):
            print("Too low, try again")
        else:
            print("Too high, try again")

main()