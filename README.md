# DecoratorUtilities

## Menu

- [Intro](#intro)
- [Installation](#installation)
- [Usage](#usage)
    - [Check Parameters Type](#check-parameters-type)
    - [Check Return Type](#check-return-type)
    - [Overloading](#overloading)
    - [Mocking functions](#mocking-functions)

## Intro
DecoratorUtilities is a python library to user type guard utilities 
to check parameters and return type, allow function overloading 
and function mocking at runtime

## Installation

```bash
pip install decoratorutilities
```

## Usage

### Check Parameters Type

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

### Check Return Type

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

### Overloading

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

### Mocking functions

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