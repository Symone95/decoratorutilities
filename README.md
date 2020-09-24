# DecoratorUtilities

## Menu

- [Intro](#intro)
- [Installation](#installation)
- [Decorators](#decorators)
    - [Check Type Decorator](#check_type_decorator)
    - [Overloading Decorator](#overloading_decorator)
    - [Mocking Decorator](#mocking-decorator)
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

# Correct invoke
my_functon(5, 6)

# Throws TypeError Exception
my_functon("5", "6")
my_functon("invalid", b="Invalid")
my_functon(a="invalid", b="Invalid")
```

##### Decorate your own function with **@checktype** decorator to check return type too

```python
from decoratorutilities import checktype

@checktype
def my_functon(a: int, b: int) -> int:
    return 1

# Correct invoke
assert my_functon(5, 6) == 1
# Throws TypeError Exception
assert my_functon(5, 6) == "1"
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

# Correct invocations
assert a(1, 2, 3, a=1) == 1
assert a(4, 5, 6, b=2) == 2

# Throws KeyError Exception
assert a(7, 8, 9, c=1) == 1
```

### Readthedocs Reference

Please read our documentation here: [Readthedocs Reference](#https://decoratorutilities.readthedocs.io/en/dev/)