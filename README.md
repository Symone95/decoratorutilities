# DecoratorUtilities

## Menu

- [Intro](#intro)
- [Installation](#installation)
- [Decorators](#decorators)
    - [Check Type Decorator](#check_type_decorator)
    - [Overloading Decorator](#overloading_decorator)
    - [Mocking Decorator](#mocking-decorator)
    - [Cached Decorator](#cached-decorator)
- [Readthedocs Reference](#readthedocs-reference)

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

@cached
def fun2(p2: str, p3: str):
   return p2

# Valid usage
fun2("ciao2", "ciao3")  # Return p2 and save it in cache
fun2("ciao2", "ciao3")  # Get return from cache
```   


### Readthedocs Reference

Please read our documentation here: [Readthedocs Reference](https://decoratorutilities.readthedocs.io/en/dev/)