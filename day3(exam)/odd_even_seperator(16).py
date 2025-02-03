def display(even_list,odd_list):
    if(not even_list):
        print("There are no even numbers in the list")
    else:
        print(f"The even numbers in the list are:\n{even_list}")
    if(not odd_list):
        print("There are no odd numbers in the list")
    else:
        print(f"The odd numbers in the list are:\n{odd_list}")
def odd_even_seperator(lst,n):
    even_list=[]
    odd_list=[]
    for i in lst:
        if(i%2==0):
            even_list.append(i)
        else:
            odd_list.append(i)
    return (even_list,odd_list)
def main():
    n=int(input("Enter the max number of elements: "))
    lst=list(map(int,input(f"Enter the {n} element of the list:\n").split()))
    even_list,odd_list=odd_even_seperator(lst,n)
    display(even_list,odd_list)
main()