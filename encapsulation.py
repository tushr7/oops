"""
1. Encapsulation

Definition Encapsulation involves bundling the data (attributes) and methods (functions) that
operate on the data into a single unit or class. It also involves restricting direct access to some of the object's
components, which can help prevent unintended interference and misuse. Link to Other Concepts

    Abstraction: Encapsulation supports abstraction by hiding the internal implementation details of an object and
    exposing only the necessary parts. This allows the object to present a simple interface to the outside world
    while maintaining its complex internal workings.

    Inheritance: Encapsulation is crucial in inheritance because it
    ensures that subclasses interact with the base class through well-defined interfaces rather than accessing
    internal data directly. This keeps the base class's implementation hidden and protected.

    Polymorphism:
    Encapsulation ensures that different classes can be used interchangeably through polymorphism by defining common
    interfaces while hiding their specific implementations. This allows polymorphism to work effectively, as objects
    can be treated uniformly based on their interfaces.
"""


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Accessing private attribute
            print(f"Deposited ${amount} into account {self.__account_number}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:  # Accessing private attribute
            self.__balance -= amount
            print(f"Withdrew ${amount} from account {self.__account_number}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Account {self.__account_number} balance: ${self.__balance}")


# Usage
account = BankAccount("12345", 1000)
account.deposit(500)  # Output: Deposited $500 into account 12345
account.withdraw(200)  # Output: Withdrew $200 from account 12345
account.check_balance()  # Output: Account 12345 balance: $1300
