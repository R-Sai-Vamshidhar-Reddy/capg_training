def display(max_value,index):
    print(f"max value is {max_value}")
    print(f"{chr(96+index)} is largest")
def get_input(n):
    maxx=0
    j=1
    for i in range(1,n+1):
        m=int(input())
        if(m>=maxx):
            maxx=m
            j=i
    return (maxx,j)
def main():
    n=int(input("no of elements: "))
    max_value,index=get_input(n)
    display(max_value,index)
main()