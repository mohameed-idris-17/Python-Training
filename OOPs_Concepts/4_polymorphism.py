# Example B: Payment Processing (Polymorphism)
# What’s being polymorphic: the pay method, which is defined in the Payment base class and implemented differently by each payment type.
# What’s specialized: each subclass (CreditCard, PayPal, BankTransfer) provides its own version of pay to handle payments in its unique way.
# What’s exposed: a common interface (pay) that lets you process payments without worrying about the underlying method.
# How it works conceptually: you can treat all payment types uniformly, calling pay on any of them, and the correct behavior happens automatically.
# Why it matters: simplifies code that uses payments, makes it easy to add new payment methods, and ensures flexible, interchangeable processing.
# One-liner for interview: “Polymorphism lets you handle different payment types with a single interface, so adding or using new methods is seamless and consistent.
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
