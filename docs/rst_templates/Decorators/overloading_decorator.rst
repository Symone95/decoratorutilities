*********************
Overloading Decorator
*********************

| Decorate your own function with **@overload** decorator to define multiple functions with same name but with different parameters
| **Example:**

.. code-block:: python
   :linenos:

    from decoratorutilities import overload

   @overload
   def my_functon(a:int):
       return 1

   @overload
   def my_functon(a:str):
       return 2

   # Valid usage
   my_functon(1)  # Invoke first my_functon and return 1
   my_functon('1')  # Invoke second my_functon and return 2

   # Invalid usage
   my_functon([1, 2, 3, 4, 5])  # Raises ValueError Exception


| Decorate your own class method with **@overload** decorator to define multiple class methods with same name but with different parameters
| **Example:**

.. code-block:: python
   :linenos:

   from decoratorutilities import overload

   class X(object):
       @overload
       def x(self, x: int):
           return int

       @overload
       def x(self, x: str):
           return str

   assert X().x(1) == int  # True
   assert X().x('1') == str  # True