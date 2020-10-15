******************
Memoized Decorator
******************

| Decorate your own function or class method with **@memoized** decorator to speed up it by storing the results and returning the cached result when the same inputs occur again
| **Example:**

.. code-block:: python
   :linenos:

   from decoratorutilities import memoized
   import datetime

   def util_run_function_with_time(fn, args, kwargs):
       start_time = datetime.datetime.now()
       tmp = fn(*args, **kwargs)
       end_time = datetime.datetime.now()
       return (end_time - start_time), tmp

   @memoized
   def memoized_fibonacci(x):
       if x == 0:
           return 0

       if x == 1:
           return 1

       return memoized_fibonacci(x - 1) + memoized_fibonacci(x - 2)

   def fibonacci(x):
       if x == 0:
           return 0

       if x == 1:
           return 1

       return fibonacci(x - 1) + fibonacci(x - 2)

   fib_value = 20
   memoized_execution_time, memoized_value = util_run_function_with_time(memoized_fibonacci, (fib_value, ), {})  # Return execution time and value for memoized function
   unmemoized_execution_time, unmemoized_value = util_run_function_with_time(fibonacci, (fib_value, ), {})  # Return execution time and value for unmemoized function

   print(f"memoized_execution_time: {memoized_execution_time} - unmemoized_execution_time: {unmemoized_execution_time}")

   assert memoized_execution_time < unmemoized_execution_time  # True
   assert memoized_value == unmemoized_value  # True
