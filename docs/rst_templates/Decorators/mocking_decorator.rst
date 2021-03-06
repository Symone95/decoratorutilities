*****************
Mocking Decorator
*****************

| Decorate your own function with **@mocking** decorator to mock that function adding args in a tuple, kwargs in a dict and return value
| **Example:**

.. code-block:: python
   :linenos:

    from decoratorutilities import mocking

   # Define args tuple, kwargs dict and return value
   @mocking([
       ((1, 2, 3), {"a": 1}, 1),
       ((4, 5, 6), {"b": 2}, 2)
   ])
   def a():
       pass

   # Valid usage
   assert a(1, 2, 3, a=1) == 1  # return 1
   assert a(4, 5, 6, b=2) == 2  # return 2

   # Invalid usage
   assert a(7, 8, 9, c=1) == 1  # Raises KeyError Exception

