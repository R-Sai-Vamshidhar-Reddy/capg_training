class Payment:
    def process_payment(self, amount):
        print("This is main class")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ₹{amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ₹{amount}")

class BitcoinPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Bitcoin payment of ₹{amount}")

# Example usage:
payments = [CreditCardPayment(), PayPalPayment(), BitcoinPayment()]
for payment in payments:
    payment.process_payment(100)


