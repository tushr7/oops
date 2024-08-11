"""
2. Inheritance

Definition Inheritance allows one class (the subclass or derived class) to inherit attributes and
methods from another class (the superclass or base class). It promotes code reusability and establishes a
hierarchical relationship between classes. Link to Other Concepts

    Encapsulation: Inheritance relies on encapsulation to ensure that base class data is protected and accessed
    appropriately by derived classes. The base class's internal state is kept hidden, while derived classes can
    extend its functionality.

    Abstraction: Inheritance enables abstraction by allowing subclasses to provide specific
    implementations of abstract methods defined in abstract base classes. This helps in creating a generalized
    interface while implementing detailed behaviors in subclasses.

    Polymorphism: Inheritance is a key enabler of
    polymorphism. Derived classes can override methods from their base classes, allowing a base class reference to
    invoke methods of derived class instances, thereby supporting polymorphic behavior.
"""

class PaymentMethod:
    def process(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class CreditCard(PaymentMethod):
    def process(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPal(PaymentMethod):
    def process(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Usage
methods = [CreditCard(), PayPal()]
for method in methods:
    method.process(100)  # Output: Processing credit card payment of $100
                         #         Processing PayPal payment of $100
