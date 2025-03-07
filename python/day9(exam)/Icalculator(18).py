from abc import ABC,abstractmethod
class ICalculator(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def substract(self):
        pass

    @abstractmethod
    def multiply(self):
        pass

    @abstractmethod
    def divide(self):
        pass

class Calculator(ICalculator):
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2

    def add(self):
        return self.number1+self.number2

    def substract(self):
        return self.number1-self.number2

    def multiply(self):
        return self.number1*self.number2
    def divide(self):
        return round(self.number1/self.number2,2)
    

n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
cal=Calculator(n1,n2)
while True:
    print("Enter 1.add\n2.substract\n3.multiply\n4.divide\n")
    n=int(input())
    if(n==1):
        print(f"Addition of {n1} and {n2} is: {cal.add()}")
    elif(n==2):
        print(f"Substraction of {n1} and {n2} is: {cal.substract()}")
    elif(n==3):
        print(f"Multiplication of {n1} and {n2} is: {cal.multiply()}")
    elif(n==4):
        print(f"division of {n1} and {n2} is: {cal.divide()}")
    else:
        break