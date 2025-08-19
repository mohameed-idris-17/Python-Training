# Example B: Payment Processing (Polymorphism)
class Payment:
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"

class PayPal(Payment):
    def pay(self, amount):
        return f"Paid {amount} using PayPal"

class BankTransfer(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Bank Transfer"

payments = [CreditCard(), PayPal(), BankTransfer()]
for method in payments:
    print(method.pay(1000))
