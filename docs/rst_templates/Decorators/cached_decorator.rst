****************
Cached Decorator
****************

Decorate your own function with **@cached** decorator
to save return in cache and use it for next time

.. code-block:: python
   :linenos:

   from decoratorutilities import cached


   @cached
   def fun2(p2: str, p3: str):
      return p2

   # Valid usage
   fun2("ciao2", "ciao3")  # Return p2 and save it in cache
   fun2("ciao2", "ciao3")  # Get return from cache
