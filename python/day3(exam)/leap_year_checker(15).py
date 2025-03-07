def check_leapyear(m):
    if(m%4==0 and m%100!=0) or (m%400==0):
        print(f"{m} is a leap year")
    else:
        print(f"{m} is not a leap year")
def get_inputs(n):
    for i in range(1,n+1):
        m=int(input(f"Enter the {i}st input: "))
        if(len(str(m))==4):
            check_leapyear(m)
        else:
            print("the input given is not valid")
            return
def main():
    n=int(input("Enter the number of inputs you to check: "))
    get_inputs(n)

main()