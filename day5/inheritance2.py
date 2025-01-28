#multiple inheritance
class Management:

    def __init(self):
        self.name="CMR"
    def display(self):
        print("This is main class")

class school(Management):
    def display_school(self):
        print("This is school")

class ug(Management):
    def display_ug(self):
        print("This is Ug")

class pg(Management):
    def display_pg(self):
        print("This is pg")
level1=school()
level2=ug()
level3=pg()
print(level3.name)
# .display()
# pg.display_school()
# pg.display_ug()
# pg.display_pg()