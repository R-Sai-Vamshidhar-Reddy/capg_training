class Cat:
    sound_cnt=0                                 #static variable
    def sound(self):
        Cat.sound_cnt+=1
        print("Meow")
class Dog:
    sound_cnt=0                                 #static variable

    def sound(self):
        Dog.sound_cnt+=1
        print("Bark")
for ani in [Cat(),Dog()]:
    ani.sound()
print(f"Cat sound called {Cat.sound_cnt}")
print(f"Dog sound called {Dog.sound_cnt}")