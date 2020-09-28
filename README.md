# DecoratorUtilities

### Readthedocs Reference

Please read our documentation here: [Readthedocs Reference](https://decoratorutilities.readthedocs.io/en/dev/)

## Menu

- [Intro](#intro)
- [Installation](#installation)
- [Decorators](#decorators)
    - [Check Type Decorator](#check_type_decorator)
    - [Overloading Decorator](#overloading_decorator)
    - [Mocking Decorator](#mocking-decorator)
    - [Cached Decorator](#cached-decorator)
    - [Timeit Decorator](#timeit-decorator)

## Intro
DecoratorUtilities is a python library to user type guard utilities 
to check parameters and return type, allow function overloading 
and function mocking at runtime

## Installation

```bash
pip install decoratorutilities
```

## Decorators

### Check Type Decorator

##### Decorate your own function with **@checktype** decorator to check parameters type

```python
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

# checktype decorator for classes methods
class X(object):

    @checktype
    def x(self, value: int):
        return value

assert X().x(1) == 1

with pytest.raises(TypeError):
    X().x('1')  # Raises TypeError Exception

```

##### Decorate your own function with **@checktype** decorator to check return type too

```python
from decoratorutilities import checktype

@checktype
def my_functon(a: int, b: int) -> int:
   return 1

# Valid usage
assert my_functon(5, 6) == 1  # return 1

# Invalid usage
assert my_functon(5, 6) == "1"  # Raises TypeError Exception
```

### Overloading Decorator

##### Decorate your own function with **@overload** decorator to define multiple functions with same name but with different parameters

```python
from decoratorutilities import overload

@overload
def my_functon(a:int):
    return 1

@overload
def my_functon(a:str):
    return 2

# Invoke first my_functon and return 1
my_functon(1)
# Invoke second my_functon and return 2
my_functon('1')
```

### Mocking Decorator

##### Decorate your own function with **@mocking** decorator to mock that function adding args in a tuple, kwargs in a dict and return value

```python
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
```

### Cached Decorator

##### Decorate your own function with **@cached** decorator to save return value in cache and reuse it for next time

```python
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

assert cached_execution_time < uncached_execution_time  # OK
assert cached_value == uncached_value  # OK
```   

### Timeit Decorator

##### Decorate your own function with **@timeit** decorator to monitoring execution time

```python
from decoratorutilities import timeit
import time


@timeit
def hello():
    time.sleep(0.1)


if __name__ == "__main__":
    hello()
```
