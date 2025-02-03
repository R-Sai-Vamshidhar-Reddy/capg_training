def table_generator(a,b,n):
    for i in range(a,b+1):
        print(f"{n} x {i} = {n*i}")
def main():
    n=int(input("Enter the table you want to generate: "))
    print("Initially it will generate in range from 1 to 10")
    print("Do you want to change the range(yes/no)?")
    m=input()
    if(m=="YES" or m=="yes"):
        a=int(input("Enter the initial Range: "))
        b=int(input("Enter the final Range: "))
        table_generator(a,b,n)
    else:
        table_generator(1,10,n)
main()