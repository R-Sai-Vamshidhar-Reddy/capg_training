class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock

    def check_quantity(self,quantity):
        if(quantity<=self.stock):
            print("The product is in stock")
        else:
            print(f"The product is not in stock and available stock is {self.stock}")

n=int(input("Enter number of inputs: "))
for i in range(n):
    name=input("Enter the name: ")
    price=float(input("Enter the price: "))
    stock=int(input("Enter the stock: "))
    obj=Product(name, price,stock)
    n=int(input("Enter the quantity: "))
    obj.check_quantity(n)