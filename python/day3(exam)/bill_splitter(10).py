def display(val):
    print(f"Each person has to pay {val} rupees")
def split_bill(t,m,tip):
    tip_amount=t*(tip/100)
    split_amount=(t+tip_amount)/m
    return split_amount

def main():
    t_bill=float(input("Enter the total bill: "))
    members=int(input("Enter the total number of people: "))
    any_tip=float(input("enter tip percentage: "))
    val=split_bill(t_bill,members,any_tip)
    display(val)
main()