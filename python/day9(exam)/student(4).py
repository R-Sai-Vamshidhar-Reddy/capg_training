class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def display(self):
        print(f"name:{self.name} rollno:{self.roll_no}")

n=int(input("Enter number of inputs: "))
for i in range(n):
    name=input("Enter the name: ")
    roll_no=int(input("Enter the roll Number: "))
    obj=Student(name,roll_no)
    obj.display()