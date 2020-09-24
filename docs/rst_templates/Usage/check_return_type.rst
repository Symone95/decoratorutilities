=================
Check Return Type
=================

Decorate your own function with @checktype decorator to check return type

.. code-block:: python
   :linenos:

    from decoratorutilities import checktype

   @checktype
   def my_functon(a: int, b: int) -> int:
       return 1

   # Correct invoke
   assert my_functon(5, 6) == 1
   # Throws TypeError Exception
   assert my_functon(5, 6) == "1"

