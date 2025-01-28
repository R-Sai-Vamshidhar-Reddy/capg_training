#Single Inheritance

class Parent:
    def __init__(self,bigNose):
        self.bigNose=bigNose
    
    def display_parent(self):
        print("This is the parent class.")

class Child(Parent):
    def __init__(self,bigNose):
        super().__init__(bigNose)
    def display_child(self):
        print("This is the child class.")

p=Parent("9CM")
c=Child("8CM")
c.display_parent()
c.display_child()
print(c.bigNose)
print(p.bigNose)