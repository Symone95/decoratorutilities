*******************
Singleton Decorator
*******************

| Decorate your own classes with **@singleton()** decorator to ensure that only one instance of the singleton class ever exists.
| Never invoke **@singleton()** decorator without brackets otherwise it will cause problems
| Define your `__init__()` class method without parameter, pass them to the **@singleton()** decorator in the format key = "value" like kwargs.
| **Example:**

.. code-block:: python
   :linenos:

   import pytest
   from decoratorutilities import singleton

   @singleton()
    class A(object):
        def __init__(self):
            self.x = 10  # Define constant class attribute

        def print_hello(self):  # Custom method
            return "Hello World"

    # Valid usage
    assert A.x == 10  # True
    assert A.print_hello() == "Hello World"  # True

    with pytest.raises(TypeError):
        # Invalid usare, brackets are missing
        @singleton
        class B(object):
            def __init__(self):
                self.x = 10

        B()  # Raises TypeError Exception


| **Example with key = "value" parameters**

.. code-block:: python
   :linenos:

   from decoratorutilities import singleton

   @singleton(x=10, message="Message to send", email=["simone.scalamandre95@gmail.com"])
   class A(object):
      pass

   # Valid usage
   assert A.x == 10  # True
   assert A.message == "Message to send"  # True
   assert len(A.email) == 1  # True
   assert A.email == ["simone.scalamandre95@gmail.com"]  # True


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