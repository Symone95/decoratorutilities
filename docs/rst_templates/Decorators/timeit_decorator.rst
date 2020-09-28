*********************
Timeit Decorator
*********************

Decorate your own function with **@timeit** decorator to monitoring execution time

.. code-block:: python
   :linenos:

   from decoratorutilities import timeit
   import time


   @timeit
   def hello():
       time.sleep(0.1)


   if __name__ == "__main__":
       hello()