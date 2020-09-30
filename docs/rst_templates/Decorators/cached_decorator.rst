****************
Cached Decorator
****************

| Decorate your own function with **@cached** decorator to save return value in cache and reuse it for next time
| **Example:**

.. code-block:: python
   :linenos:

   from decoratorutilities import cached
   import datetime

   def util_run_function_with_time(fn, args, kwargs):
       start_time = datetime.datetime.now()
       tmp = fn(*args, **kwargs)
       end_time = datetime.datetime.now()
       return (end_time - start_time), tmp

   @cached
   def cached_fibonacci(x):
       if x == 0:
           return 0

       if x == 1:
           return 1

       return cached_fibonacci(x - 1) + cached_fibonacci(x - 2)

   def fibonacci(x):
       if x == 0:
           return 0

       if x == 1:
           return 1

       return fibonacci(x - 1) + fibonacci(x - 2)

   fib_value = 20
   cached_execution_time, cached_value = util_run_function_with_time(cached_fibonacci, (fib_value, ), {})  # Return execution time and value for cached function
   uncached_execution_time, uncached_value = util_run_function_with_time(fibonacci, (fib_value, ), {})  # Return execution time and value for uncached function

   print(f"cached_execution_time: {cached_execution_time} - uncached_execution_time: {uncached_execution_time}")

   assert cached_execution_time < uncached_execution_time  # True
   assert cached_value == uncached_value  # True
