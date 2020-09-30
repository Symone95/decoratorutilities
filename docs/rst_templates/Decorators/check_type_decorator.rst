********************
Check Type Decorator
********************

| Decorate your own function with **@checktype** decorator to check parameters type
| **Example:**

.. code-block:: python
   :linenos:

    from decoratorutilities import checktype

    @checktype
    def my_functon(a: int, b: int):
        return 1

    # Valid usage
    my_functon(5, 6)  # return 1

    # Invalid usage
    my_functon("5", "6")  # Raises TypeError Exception
    my_functon("invalid", b="Invalid")  # Raises TypeError Exception
    my_functon(a="invalid", b="Invalid")  # Raises TypeError Exception


| Decorate your own function with **@checktype** decorator to check return type too
| **Example:**

.. code-block:: python
   :linenos:

   from decoratorutilities import checktype

   @checktype
   def my_functon(a: int, b: int) -> int:
       return 1

   # Valid usage
   assert my_functon(5, 6) == 1  # return 1

   # Invalid usage
   assert my_functon(5, 6) == "1"  # Raises TypeError Exception


| Decorate your own class methods with **@checktype** decorator to check parameters and return type
| **Example:**

.. code-block:: python
   :linenos:

   class X(object):

       @checktype
       def x(self, value: int):
           return value

   assert X().x(1) == 1

   with pytest.raises(TypeError):
       X().x('1')  # Raises TypeError Exception
