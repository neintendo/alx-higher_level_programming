# 0x06. Python Classes

**0-square.py:** an empty class `Square` that defines a square.

**1-square.py:** a class `Square` that defines a square by: (based on `0-square.py`).

- Private instance attribute: `size.`
- Instantiation with `size` (no type/value verification).

**2-square.py:** a class `Square` that defines a square by: (based on `1-square.py`).

- Private instance attribute: `size`.
- Instantiation with optional `size`: `def __init__(self, size=0):`.
- `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.
- If `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`.

**3-square.py:** a class `Square` that defines a square by: (based on `2-square.py`).

- Private instance attribute: `size`.
- Instantiation with optional `size`: `def __init__(self, size=0):`.
- `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.
- If `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`.
- Public instance method: `def area(self):` that returns the current square area.

**4-square.py:** a class `Square` that defines a square by: (`based on 3-square.py`)

- Private instance attribute: `size`:
  - Property `def size(self):` to retrieve it.
  - Property setter `def size(self, value):` to set it:
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.
    - If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.
- Instantiation with optional `size`: `def __init__(self, size=0):`.
- Public instance method: `def area(self):` that returns the current square area.

**5-square.py:** a class `Square` that defines a square by: (`based on 4-square.py`)

- Private instance attribute: `size`:
  - Property `def size(self):` to retrieve it.
  - Property setter `def size(self, value):` to set it:
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.
    - If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.
- Instantiation with optional `size`: `def __init__(self, size=0):`.
- Public instance method: `def area(self):` that returns the current square area.
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
  - If `size` is equal to `0`, print an empty line.
