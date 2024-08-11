"""
Sticking to the design principles of composition and using method delegation is generally the best practice. This approach maintains the integrity of the component classes and promotes better code organization, readability, and maintainability. Here’s a deeper look at why this approach is advantageous:
Advantages of Method Delegation in Composition

    Encapsulation: By using composition and delegating method calls to component classes, you encapsulate the
    behavior of each component. This means that the internal workings of each component are hidden from the composite
    class, reducing complexity.

    Single Responsibility Principle: Each class (both composite and component) has a
    clear responsibility. The component classes handle their own behaviors, while the composite class manages how
    these components are used together. This separation of concerns makes the code easier to understand and maintain.

    Flexibility and Reusability: Delegating method calls allows you to reuse component classes in different contexts
    or with different composite classes without modifying their behavior. This promotes code reuse and makes it
    easier to swap out components if needed.

    Maintainability: If you need to change the behavior of a component,
    you can do so in the component class itself without affecting the composite class. This reduces the risk of
    introducing bugs and makes the system easier to maintain.

    Clearer Interfaces: When using delegation,
    the composite class can provide a clear interface for interacting with the components. This makes it easier for
    other developers (or your future self) to understand how to use the composite class without needing to dive into
    the details of the component classes."""


class CardReader:
    def read_card(self):
        return "Card information read."


class TransactionProcessor:
    def process_transaction(self, card_info):
        return f"Processing transaction for {card_info}."


class SecurityModule:
    def encrypt(self, data):
        return f"Encrypted data: {data}"


class PaymentGateway:
    def __init__(self):
        self.card_reader = CardReader()  # PaymentGateway has a CardReader
        self.transaction_processor = TransactionProcessor()  # PaymentGateway has a TransactionProcessor
        self.security_module = SecurityModule()  # PaymentGateway has a SecurityModule

    def process_payment(self):
        card_info = self.card_reader.read_card()  # Step 1: Read card information
        encrypted_info = self.security_module.encrypt(card_info)  # Step 2: Encrypt the information
        transaction_status = self.transaction_processor.process_transaction(encrypted_info)  # Step 3: Process the
        # transaction
        return transaction_status


# Usage
gateway = PaymentGateway()
result = gateway.process_payment()
print(result)  # Output: Processing transaction for Encrypted data: Card information read.
