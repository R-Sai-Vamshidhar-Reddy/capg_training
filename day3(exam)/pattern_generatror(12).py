def pattern_generator_reverse(n):
    for i in range(n,0,-1):
        print("*"*i)
def pattern_generator(n):
    for i in range(1,n+1):
        print("*"*i)
def main():
    n=int(input("Enter the number to get the pattern: "))
    if(n<=0):
        print("The input should be greater than 0")
    else:
        ans=pattern_generator(n)
    print("Do you want to generator pattern in reverse(yes/no)?")
    m=input()
    if(m=="yes" or m=="YES"):
        pattern_generator_reverse(n)
    else:
        print(":)")
main()