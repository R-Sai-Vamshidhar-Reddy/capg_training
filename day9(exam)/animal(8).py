class Animal:
    def speak(self):
        print("It is an animal")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("It is a Dog")

class Cat(Animal):
    def speak(self):
        print("It is a cat")



obj1=Cat()
obj1.speak()
obj2=Dog()
obj2.speak()
