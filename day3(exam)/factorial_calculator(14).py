def display(ans,n):
    print(f"The factorial of {n} is :{ans}")
def find_fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def main():
    n=int(input("Enter the number to find the factorial: "))
    if(n<0):
        print("The input should be greater than 0")
    else:
        ans=find_fact(n)
        display(ans,n)
main()