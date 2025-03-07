
class Management:

    def __init__(self):
        self.namee="CMR"
    def display(self):
        print("This is main class")

class school(Management):
    def display_school(self):
        print("This is school")

class ug(school):
    def display_ug(self):
        print("This is Ug")

class pg(ug):
    # def __init__(self):
    #     super().__init__(self)
    def display_pg(self):
        print("This is pg")


obj=pg()
obj.display()
obj.display_ug()