"""
3. Polymorphism

Definition Polymorphism allows objects of different classes to be treated as objects of a common base class. It
enables methods to perform different functions based on the object they are acting upon, even though they share the
same method name. Link to Other Concepts

    Encapsulation: Polymorphism works within the framework of encapsulation, as it relies on interacting with objects
    through their public interfaces while encapsulating the details. This allows for flexible and dynamic method
    invocation based on object types.

    Inheritance: Polymorphism is closely related to inheritance, as it often
    involves overriding methods in derived classes. The base class provides a common interface, while derived classes
    provide specific implementations, which can be invoked polymorphically.

    Abstraction: Polymorphism supports
    abstraction by allowing operations to be performed on objects of different types without knowing their specific
    class. It provides a unified interface for various objects, abstracting away their underlying details.

"""


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Usage
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area of {type(shape).__name__}: {shape.area()}")  # Output: Area of Circle: 78.5
    #         Area of Rectangle: 24
