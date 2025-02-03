def check_prime(n):
    if(n>2):
        for i in range(2,int(n**(0.5))+1):
            if(n%i==0):
                return False
        return True
    elif(n==2):
        print("2 is a least prime number")
    else:
        return False
def main():
    a=int(input("Enter the starting range: "))
    b=int(input("Enter the ending range: "))
    if(a<b and a>0 and b>0):
        for i in range(a,b+1):
            if(check_prime(i)):
                print(f"{i} is prime number")
    else:
        print("the input should be greater than 2/the first input should be smaller than second input")
main()