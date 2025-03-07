class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"names: {self.name}")
        print(f"salary: {self.salary}")
class Student:
    def __init__(self,name,cls):
        self.name=name
        self.cls=cls

    def __repr__(self):                 #__repr__ is a method which is used to debug and understand
        return f"{self.name} class is {self.cls}"    
# emp1=Employee("Vara",2000)
# emp2=Employee("Sai",3000)
# lst=[emp1,emp2]
# print(lst[0])
# print(lst[1])
# print(lst[0].name)
# print(lst[0].salary)
# emp2.display()

details=Employee(["sai","vamshi","vara"],[2000,3000,4000])
details.display()
stu=Student("vara","Btech")
stu2=Student("Sai","btech")
lst=[stu,stu2]
print(lst)