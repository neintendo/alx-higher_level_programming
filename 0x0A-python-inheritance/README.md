# 0x0A. Python: Inheritance

**0-lookup.py:** a function that returns the list of available attributes and methods of an object:

- Prototype: `def lookup(obj):`.
- Returns a `list` object.

**1-my_list.py:** a class `MyList` that inherits from `list`:

- Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort).

**2-is_same_class.py:** a function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`.

- Prototype: `def is_same_class(obj, a_class):`

**3-is_kind_of_class.py:** a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.

- Prototype: `def is_kind_of_class(obj, a_class):`

**4-inherits_from.py:** a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.

- Prototype: `def inherits_from(obj, a_class):`

**5-base_geometry.py:** an empty class `BaseGeometry`.

**6-base_geometry.py:** a class `BaseGeometry` (based on `5-base_geometry.py`).

- Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`.

**7-base_geometry.py:** a class `BaseGeometry` (based on `6-base_geometry.py`).

- Public instance method: `def area(self):` that raises an Exception with the message `area() is not implemented`.
- Public instance method: `def integer_validator(self, name, value):` that validates `value`:
- If `value` is not an integer: raise a `TypeError` exception, with the `message <name> must be an integer`.
- If `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`.

**8-base_geometry.py:** a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).

- Instantiation with `width` and `height`: `def __init__(self, width, height):`

**9-rectangle.py:** a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)

- Instantiation with `width` and `height`: `def __init__(self, width, height):`:
  - `width` and `height` must be private. No getter or setter.
  - `width` and `height` must be positive integers validated by `integer_validator`.
- `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

**10-square.py:** a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):

- Instantiation with `size`: `def __init__(self, size):`:
  - `size` must be private. No getter or setter.
  - `size` must be a positive integer, validated by `integer_validator`.
- The `area()` method must be implemented

**11-square.py:** a class `Square` that inherits from `Rectangle` (`10-sqaure.py`):

- Instantiation with `size`: `def __init__(self, size):`:
  - `size` must be private. No getter or setter.
  - `size` must be a positive integer, validated by `integer_validator`.
- The `area()` method must be implemented.
- `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`
