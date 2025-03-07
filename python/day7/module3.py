from module_1 import Man
from module_2 import Woman
class Person(Man,Woman):                    #single class have multiple parents
    pass
    def both(self):
        return "Can do both dance and sing"

person=Person()
print(person.man())
print(person.woman())
print(person.both())
w=Woman()
w=person
print(w.both())
