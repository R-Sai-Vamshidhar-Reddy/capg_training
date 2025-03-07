def display(data):
    print(f"greatest among 3 numbers is: {data}")
def get_input():
    n1=int(input("first no: "))
    n2=int(input("second no: "))
    n3=int(input("third no: "))
    return n1,n2,n3
def get_max(a,b):
    if(a>b):
        return a
    else:
        return b
def compute(n1,n2,n3):
    return get_max(get_max(n1,n2),get_max(n2,n3))
     

def main():
    n1,n2,n3=get_input()
    data=compute(n1,n2,n3)
    display(data)
main()
    