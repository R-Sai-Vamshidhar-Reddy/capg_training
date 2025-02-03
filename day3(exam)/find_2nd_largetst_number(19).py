def display(ans):
    print(f"Second largest number in list is {ans}")
def check_2nd_largest(lst,n):
    maxx=float("-inf")
    maxx2=float("-inf")
    for i in lst:
        if(i>maxx):
            maxx2=maxx
            maxx=i
        else:
            if i>maxx2 and maxx2!=maxx:
                maxx2=i
    return maxx2
def main():
    n=int(input("Enter the max number of elements: "))
    lst=list(map(int,input(f"Enter the {n} element of the list:\n").split()))
    ans=check_2nd_largest(lst,n)
    display(ans)
main()