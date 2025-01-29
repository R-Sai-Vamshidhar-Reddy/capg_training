#default constructor

class Management:

    def __init__(self): #default constuctor
        self.namee="CMR"

class school(Management):
    def display_school(self):
        print("This is school")

s=school()
print(s.namee)


#constuctor with parameters

class Manage:

    def __init__(self,value): # constuctor with parameters
        self.namee="CMR"
        self.value=value
        print(self.value)

class schl(Manage):
    def display_school(self):
        print("This is school")

sh=schl("hello")

