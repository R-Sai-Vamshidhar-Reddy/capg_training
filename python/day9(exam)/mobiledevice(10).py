class Electronics:
    def __init__(self,brand_name,color):
        self.name=brand_name
        self.color=color
    def display(self):
        print("This is Electronics class")
        print(f"brand_name:{self.brand_name}\ncolor:{self.color}")
class MobileDevices(Electronics):
    def __init__(self,brand_name,color,model):
        self.brand_name=brand_name
        self.color=color
        self.model=model
        super().__init__(brand_name,color)
    def display(self):
        super().display()
        print("\nthis is mobile devices class")
        print(f"brand_name:{self.brand_name}\ncolor:{self.color}\nmodel:{self.model}")

class SmartPhone(MobileDevices):
    def __init__(self,brand_name,color,model,screen_size):
        self.brand_name=brand_name
        self.color=color
        self.model=model
        self.screen_size=screen_size
        super().__init__(brand_name,color,model)
    def display(self):
        super().display()
        print("\nThis is smartphone class")
        print(f"brand_name:{self.brand_name}\ncolor:{self.color}\nmodel:{self.model}\nscreen_size:{self.screen_size}")
smartPhone=SmartPhone("samung","white","S24","16inches")
smartPhone.display()

