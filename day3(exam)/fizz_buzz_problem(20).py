def fizz_buzz(x,y):
    for i in range(x,y+1):
        if(i%3==0 and i%5==0):
            print(f"{i}-fizzbuzz")
        elif(i%3==0):
            print(f"{i}-fizz")
        elif(i%5==0):
            print(f"{i}-buzz")
def main():
    print("Initially the range is b/w 1 and 100")
    print("do you what to change the range(yes/no)?")
    n=input()
    if(n=="YES" or n=="yes"):
        a=int(input("Enter the starting range: "))
        b=int(input("Enter the ending range: "))
        if(a<b and a>0 and b>0):
            fizz_buzz(a,b)
        else:
            print("the input should be greater than 2/the first input should be smaller than second input")
    else:
        fizz_buzz(1,100)
main()