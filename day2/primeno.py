def check_prime(n):
    if(n>2):
        for i in range(3,int(n**(0.5))+1):
            if(n%i==0):
                return False
        return True
    elif(n==2):
        print("2 is a least prime number")
    else:
        return False
def main():
    n=int(input())
    if(check_prime(n)):
        print("It is a prime number")
    else:
        print("It is not a prime number")
main()