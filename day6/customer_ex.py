
class Customer:
    def __init__(self, customer_id, first_name, last_name, phone, email):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.orders = []  # List to store customer's orders

    def add_order(self, order):
        self.orders.append(order)

    def display(self):
        print("\nCustomer Details:")
        print(f"Customer ID: {self.customer_id}")
        print(f"Customer Name: {self.first_name} {self.last_name}")
        print(f"Phone Number: {self.phone}")
        print(f"Email: {self.email}")
        print("Orders:")
        for order in self.orders:
            print(f"  - Order ID: {order.order_id}, Status: {order.order_status}")
        print("-" * 30)


class Order:
    def __init__(self, order_id, customer, order_status):
        self.order_id = order_id
        self.customer = customer  # Link to a Customer object
        self.order_status = order_status
        self.transactions = []  # List to store transactions

        # Automatically add this order to the customer's order list
        customer.add_order(self)

    def add_transaction(self, transaction):
        
        self.transactions.append(transaction)

    def display(self):
        print("\nOrder Details:")
        print(f"Order ID: {self.order_id}")
        print(f"Customer ID: {self.customer.customer_id} ({self.customer.first_name} {self.customer.last_name})")
        print(f"Order Status: {self.order_status}")
        print("Transactions:")
        for transaction in self.transactions:
            print(f"  - Transaction ID: {transaction.transaction_id}")
        print("-" * 30)


class Transaction:
    def __init__(self, transaction_id, order):
        self.transaction_id = transaction_id
        self.order = order  # Link to an Order object

        # Automatically add this transaction to the order's transaction list
        order.add_transaction(self)

    def display(self):
        print("\nTransaction Details:")
        print(f"Transaction ID: {self.transaction_id}")
        print(f"Order ID: {self.order.order_id}")
        print(f"Customer ID: {self.order.customer.customer_id} ({self.order.customer.first_name} {self.order.customer.last_name})")
        print("-" * 30)




# Taking Customer Input
customer_id = int(input("Enter Customer ID: "))
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")

# Creating a Customer Object
customer1 = Customer(customer_id, first_name, last_name, phone, email)

# Taking Order Inputs
num_orders = int(input("Enter number of orders: "))

orders = []
for _ in range(num_orders):
    order_id = int(input("\nEnter Order ID: "))
    order_status = input("Enter Order Status (Pending/Completed/etc.): ")
    order = Order(order_id, customer1, order_status)
    orders.append(order)

# Taking Transaction Inputs
for order in orders:
    num_transactions = int(input(f"\nEnter number of transactions for Order {order.order_id}: "))
    for _ in range(num_transactions):
        transaction_id = int(input("Enter Transaction ID: "))
        Transaction(transaction_id, order)


customer1.display()
for order in orders:
    order.display()
    for transaction in order.transactions:
        transaction.display()
