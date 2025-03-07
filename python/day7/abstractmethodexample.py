from abc import ABC,abstractmethod               #abc is (abstract base class)
class Father(ABC):                   #abstract class
    @abstractmethod
    def disp(self):                 #abstract method
        print("abstract")
    def show(self):
        print("concreate method") #Method which is alreadyimplemented in abstract class is known as concreate method
        

class Son(Father):
    def disp(self):
        super().disp()
        print("Son is implementing the abstact method")


class Daughter(Father):
    def disp(self):
        print("Daughter is implementing the abstract method")

s=Son()
s.disp()
s.show()
d=Daughter()
d.disp()
d.show()