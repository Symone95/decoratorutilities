*******************
Singleton Decorator
*******************

| Decorate your own classes with **@singleton()** decorator to ensure that only one instance of the singleton class ever exists.
| Never invoke **@singleton()** decorator without brackets otherwise it will cause problems
| Define your `__init__()` class method without parameters, pass them to the **@singleton()** decorator
| **Example with args and kwargs:**

.. code-block:: python
   :linenos:

   import pytest
   from decoratorutilities import singleton

   @singleton(10, message="Message to send", email=["simone.scalamandre95@gmail.com"])
   class A(object):
       def __init__(self):
           self.x = 50  # Define constant class attribute

       def print_hello(self):  # Custom method
           return "Hello World"

   # Valid usage
   assert A[0] == 10  # True -> Get first arg
   assert A.x == 50  # True -> Get decorated class attribute
   assert A.print_hello() == "Hello World"  # True -> Get decorated class method "print_hello()"
   assert A.message == "Message to send"  # True -> Get kwarg "message" passed to Singleton decorator
   assert A.email == ["simone.scalamandre95@gmail.com"]  # True

   with pytest.raises(TypeError):
       # Invalid usage, brackets are missing
       @singleton
       class B(object):
           def __init__(self):
               self.x = 10

       B()  # Raises TypeError Exception


| We can define our singleton class with or without kwargs parameters but we can only instantiate one
| **Example**

.. code-block:: python
   :linenos:

   import pytest
   from decoratorutilities import singleton

   @singleton()
   class A(object):
     def __init__(self):
         pass

   @singleton(x=10)
   class B(object):
     def __init__(self):
         pass

   with pytest.raises(TypeError) as e:
      A()  # Raise TypeError Exception

   with pytest.raises(TypeError):
      B()  # Raise TypeError Exception