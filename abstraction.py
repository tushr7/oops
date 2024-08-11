"""
4. Abstraction
Definition Abstraction involves defining the essential characteristics of an object while ignoring
irrelevant details. It allows you to focus on what an object does rather than how it does it. Link to Other Concepts

    Encapsulation: Abstraction relies on encapsulation to hide the internal implementation details and expose only
    the relevant aspects of an object. Encapsulation provides the means to enforce abstraction by keeping details
    private and providing a controlled interface.

    Inheritance: Abstraction is implemented through inheritance by
    defining abstract classes with abstract methods. Subclasses then provide concrete implementations of these
    abstract methods, enabling a generalized interface and specific behaviors.

    Polymorphism: Abstraction and
    polymorphism work together to provide a flexible interface. Polymorphism allows different objects to be used
    interchangeably through their abstract interfaces, while abstraction ensures that only relevant details are
    exposed.

"""

from abc import ABC, abstractmethod


class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass


class MySQLConnector(DatabaseConnector):
    def connect(self):
        print("Connecting to MySQL database...")

    def execute_query(self, query):
        print(f"Executing MySQL query: {query}")


class PostgreSQLConnector(DatabaseConnector):
    def connect(self):
        print("Connecting to PostgresSQL database...")

    def execute_query(self, query):
        print(f"Executing PostgresSQL query: {query}")


# Usage
def run_query(connector: DatabaseConnector, query):
    connector.connect()
    connector.execute_query(query)


mysql_connector = MySQLConnector()
postgresql_connector = PostgreSQLConnector()

run_query(mysql_connector, "SELECT * FROM users")  # Output: Connecting to MySQL database...
#         Executing MySQL query: SELECT * FROM users
run_query(postgresql_connector, "SELECT * FROM products")  # Output: Connecting to PostgresSQL database...
#         Executing PostgresSQL query: SELECT * FROM products
