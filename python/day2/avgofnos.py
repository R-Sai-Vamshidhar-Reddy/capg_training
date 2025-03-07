def display(data):
    print(f"avg of 4 no's is {data}")
def compute(n1,n2,n3,n4):
    avg=(n1+n2+n3+n4)/4 #calculating
    return avg
def get_input():
    n1,n2,n3,n4=input().split() #taking inputs
    return int(n1),int(n2),int(n3),int(n4)
def main():
    (n1,n2,n3,n4)=get_input() #getting inputs
    avg=compute(n1,n2,n3,n4)
    display(avg)
main()