class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
    
    def display(self):
        super().display()
        print(f"Employee ID: {self.employee_id}")


class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def display(self):
        super().display()
        print(f"department: {self.department}")    
    def approve_leave(self, employee_name, days):
        print(f"Manager {self.name} approved {days} days leave for {employee_name}.")

manager = Manager("Sai", 20, "1", "HR")
manager.display()
manager.approve_leave("Vamshi", 5)



