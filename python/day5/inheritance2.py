#Hierarchical inheritance
class Management:

    def __init__(self):
        self.namee="CMR"
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
print(level3.namee)
level1.display_school()
level1.display()
level2.display_ug()
level2.display()
level3.display_pg()
level3.display()
# .display()
# pg.display_school()
# pg.display_ug()
# pg.display_pg()