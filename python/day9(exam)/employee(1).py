class Employee:
    def __init__(self,name,id,dept):
        self.name=name
        self.id=id
        self.dept=dept

    def display(self):
        print(f"{self.name} {self.id} {self.dept}")

n=int(input("Enter number of inputs: "))
for i in range(n):
    name=input("Enter the name: ")
    id=input("Enter the id: ")
    dept=input("Enter the dept: ")
    obj=Employee(name,id,dept)
    obj.display()
