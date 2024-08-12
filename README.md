* Refer to universal_remote.py*

<img width="1007" alt="image" src="https://github.com/user-attachments/assets/5bbaeca9-3fcb-4505-a1ca-c0d4d8c4576e">


# 1. Encapsulation
Definition: Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit or class, while restricting direct access to some of the object's components. In the Code:

    While the code does not explicitly define private attributes, it encapsulates the behavior of different devices (TV, DVD, AC) within their respective classes. Each device class contains methods that operate on its internal state (e.g., turning on, turning off, adjusting volume).
    You could enhance encapsulation further by adding private attributes to each class that represent the state of the device (e.g., whether the device is on or off), but this is not strictly necessary for demonstrating the concept.

# 2. Inheritance
Definition: Inheritance allows one class (the subclass) to inherit attributes and methods from another class (the superclass), promoting code reusability and establishing a hierarchical relationship. In the Code:

    The UniversalRemote class is an abstract base class that defines the interface for all remote-controlled devices.
    The TV, DVD, and AC classes inherit from UniversalRemote, implementing the abstract methods defined in the base class. This demonstrates how subclasses can extend the functionality of a base class.

# 3. Abstraction
Definition: Abstraction involves defining the essential characteristics of an object while ignoring irrelevant details. It allows you to focus on what an object does rather than how it does it. In the Code:

    The UniversalRemote class serves as an abstract class that defines the common interface for all remote-controlled devices. It specifies the methods (on, off, volume_up, volume_down) that must be implemented by any subclass.
    The subclasses (TV, DVD, AC) provide concrete implementations of these methods, allowing users to interact with the devices without needing to know the specifics of how each method works.

# 4. Polymorphism
Definition: Polymorphism allows objects of different classes to be treated as objects of a common base class. It enables methods to perform different functions based on the object they are acting upon, even though they share the same method name. In the Code:

    The operate function takes a UniversalRemote object as a parameter and calls the appropriate method based on the operation specified. This demonstrates polymorphism because the function can operate on any subclass of UniversalRemote (like TV, DVD, or AC) without knowing the specific type of device.
    Each device class implements the same interface but provides its own behavior for the methods, allowing the same method calls to yield different results based on the actual object type.

# Summary
In summary, the code effectively demonstrates:

    Encapsulation: Bundling of methods related to device operations within their respective classes.
    Inheritance: Subclasses (TV, DVD, AC) inheriting from the abstract base class (UniversalRemote).
    Abstraction: Defining a common interface in the abstract class that hides implementation details.
    Polymorphism: The operate function using a common interface to interact with different device types.
