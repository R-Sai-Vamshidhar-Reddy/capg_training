from abc import ABC, abstractmethod

# Abstract class
class Person(ABC):  
    def __init__(self, name, pan_card):
        self.name = name
        self.pan_card = pan_card
    
    @abstractmethod
    def get_pan_card(self):  # Abstract method (must be implemented by subclasses)
        pass

# Concrete class for Father
class Father(Person):
    def get_pan_card(self):
        print(f"Father {self.name} has PAN card: {self.pan_card}")

# Concrete class for Child
class Child(Person):
    def get_pan_card(self):
        print(f"Child {self.name} has PAN card: {self.pan_card}")

# Creating objects
father = Father("Rajesh", "ABCDE1234F")
child = Child("Amit", "XYZ12345G")

# Calling the method
father.get_pan_card()  # Output: Father Rajesh has PAN card: ABCDE1234F
child.get_pan_card()   # Output: Child Amit has PAN card: XYZ12345G