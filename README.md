# DecoratorUtilities

### Readthedocs Reference

Please read our documentation here: [Readthedocs Reference](https://decoratorutilities.readthedocs.io/en/dev/)

### Package Reference

Our package reference link is: https://pypi.org/project/decoratorutilities

## Menu

- [Intro](#intro)
- [Installation](#installation)
- [Decorators](#decorators)
    - [Check Type Decorator](#check_type_decorator)
    - [Overloading Decorator](#overloading_decorator)
    - [Mocking Decorator](#mocking-decorator)
    - [Memoized Decorator](#memoized-decorator)
    - [Timeit Decorator](#timeit-decorator)
    - [Singleton Decorator](#singleton-decorator)

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

Decorate your own functions with **@checktype** decorator to check parameters type and return type too
**Example:**

```python
from decoratorutilities import checktype
import pytest

@checktype
def my_functon(a: int, b: int) -> int:
    return 1

# Valid usage: Integer parameters and return type
my_functon(5, 6)  # return 1
assert my_functon(5, 6) == 1  # True

# Invalid usage: String parameters and return type
with pytest.raises(TypeError):
    my_functon("5", "6")  # Raises TypeError Exception
with pytest.raises(TypeError):
    my_functon("invalid", b="Invalid")  # Raises TypeError Exception
with pytest.raises(TypeError):
    my_functon(a="invalid", b="Invalid")  # Raises TypeError Exception
with pytest.raises(TypeError):
    assert my_functon(5, 6) == "1"  # Raises TypeError Exception
```

Decorate your own class methods with **@checktype** decorator to check parameters type and return type too
**Example:**

```python
from decoratorutilities import checktype
import pytest

class X(object):

    @checktype  # checktype decorator for classes methods
    def my_function(self, value: int):
        return value

# Valid usage: Integer parameters and return type
assert X().my_function(1) == 1  # True

# Invalid usage: String parameters and return type
with pytest.raises(TypeError):
    X().my_function('1')  # Raises TypeError Exception
with pytest.raises(TypeError):
    X().my_function(1) == "1"  # Raises TypeError Exception
```

### Overloading Decorator

Decorate your own function with **@overload** decorator to define multiple functions with same name but with different parameters  
**Example:**

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

Decorate your own class method with **@overload** decorator to define multiple class methods with same name but with different parameters  
**Example:**

```python
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
```


### Mocking Decorator

Decorate your own function with **@mocking** decorator to mock that function adding args in a tuple, kwargs in a dict and return value  
**Example:**

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

### Memoized Decorator

Decorate your own function or class method with **@memoized** decorator to speed up it by storing the results and returning the cached result when the same inputs occur again  
**Example:**

```python
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

assert memoized_execution_time < unmemoized_execution_time  # OK
assert memoized_value == unmemoized_value  # OK
```   

### Timeit Decorator

Decorate your own function with **@timeit** decorator to monitoring execution time  
**Example:**

```python
from decoratorutilities import timeit
import time


@timeit
def hello():
    time.sleep(0.1)


if __name__ == "__main__":
    hello()  # print "Execution time: 100.75 ms"
```


### Debug Decorator

Decorate your own function with **@debug** decorator to print in console more Exception details  
**Example:**

```python
from decoratorutilities import debug
import pytest

@debug
def a():
    message = "Hello " + 5
    return message

with pytest.raises(TypeError):
    a() # Print in console: Found "<class 'TypeError'>" Exception in file "('../tests', 'test_debug.py')" on line "9"
        # Error message: "can only concatenate str (not "int") to str"
```

Decorate your own class methods with **@debug** decorator to print in console more Exception details  
**Example:**

```python
from decoratorutilities import debug
import pytest

class A(object):

    @debug
    def __init__(self):
        self.message = "Hello " + 5

with pytest.raises(TypeError):
    A()  # Raises TypeError Exception
```

### Singleton Decorator

Decorate your own classes with **@singleton()** decorator to ensure that only one instance of the singleton class ever exists.
Never invoke **@singleton()** decorator without brackets otherwise it will cause problems
Define your class method `__init__()` without parameters, pass them to the **@singleton()** decorator

**Example with args and kwargs**

```python
import pytest
from decoratorutilities import singleton

@singleton(10, message="Message to send", email=["simone.scalamandre95@gmail.com"])
class A(object):
    def __init__(self):
        self.x = 50  # Define constant class attribute

    def print_hello(self):  # Custom method
        return "Hello World"

# Valid usage
assert A[0] == 10  # True -> Get first arg
assert A.x == 50  # True -> Get decorated class attribute
assert A.print_hello() == "Hello World"  # True -> Get decorated class method "print_hello()"
assert A.message == "Message to send"  # True -> Get kwarg "message" passed to Singleton decorator
assert A.email == ["simone.scalamandre95@gmail.com"]  # True

with pytest.raises(TypeError):
    # Invalid usage, brackets are missing
    @singleton
    class B(object):
        def __init__(self):
            self.x = 10

    B()  # Raises TypeError Exception
```

We can define our singleton class with or without args and kwargs parameters but we can only instantiate one
**Example**

```python
import pytest
from decoratorutilities import singleton

@singleton()
class A(object):
    def __init__(self):
        pass

@singleton(x=10)
class B(object):
    def __init__(self):
        pass

with pytest.raises(TypeError) as e:
    A()  # Raises TypeError Exception

with pytest.raises(TypeError):
    B()  # Raises TypeError Exception
```