***************
Debug Decorator
***************

| Decorate your own function with **@debug** decorator to print in console more Exception details
| **Example:**

.. code-block:: python
   :linenos:

   from decoratorutilities import debug
   import pytest

   @debug
   def a():
       message = "Hello " + 5
       return message

   with pytest.raises(TypeError):
       a() # Print in console: Found "<class 'TypeError'>" Exception in file "('../tests', 'test_debug.py')" on line "9"
           # Error message: "can only concatenate str (not "int") to str"


| Decorate your own class methods with **@debug** decorator to print in console more Exception details
| **Example:**

.. code-block:: python
   :linenos:

   from decoratorutilities import debug
   import pytest

   class A(object):

       @debug
       def __init__(self):
           self.message = "Hello " + 5

   with pytest.raises(TypeError):
       A()