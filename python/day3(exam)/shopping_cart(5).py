def add_item(cart):
    item=input("Enter the item name: ")
    price=float(input("Enter the price of item: "))
    if price > 0:
        cart.append({"name": item, "price": price})
        print(f"\n{item} added to the cart for ₹{round(price,2)}.")
    else:
        print("Price must be greater than zero.")

def view_cart_items(cart):
    if cart:
        print("\nItems in your cart:")
        for index, item in enumerate(cart, start=1):
            print(f"\n{index}. {item['name']} - ₹{item['price']:.2f}")
    else:
        print("Your cart is empty.")

def calculate_total_price(cart):
    sm=0
    for item in cart:
        sm+=item["price"]
    print(f"The total price of items in your cart is: {sm}")

def exit():
    print("Thank you\n")
def main():
    cart=[]
    while True:
        print("\nPlease enter the number from below choices")
        print("Enter 1 to add item")
        print("Enter 2 to view cart itmes")
        print("Enter 3 for calucalating total price")
        print("Enter 4 for Exit")
        n=int(input("Enter the number:"))
        if(n<0 or n>4):
            print("Invalid input")
            return
        else:
            if(n==1):
                add_item(cart)
            elif(n==2):
                view_cart_items(cart)
            elif(n==3):
                calculate_total_price(cart)
            elif(n==4):
                exit()
                break
        


main()