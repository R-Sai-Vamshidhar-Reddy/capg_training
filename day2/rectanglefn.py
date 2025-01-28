def display(data):
    print(f"the area is {data}")
def get_input():
    received_len=int(input())
    received_width=int(input())
    return (received_len,received_width)

def compute_area(length,width):
    area=int(length)*int(width)
    return area

def main():
    (length,width)=get_input()
    area=compute_area(length,width)
    display(area)
main()