class Man:
    def man(self):
        return "I am a man ,i can dance better"

class Woman:
    def woman(self):
        return "I am a woman, i can sing better"
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
