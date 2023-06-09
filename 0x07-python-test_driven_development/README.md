# 0x07. Python: Test Driven Development

**0-add_integer.py:**  a function that adds 2 integers.

- Prototype: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`.
- `a` and `b` must be first casted to integers if they are float.
- Returns an integer: the addition of `a` and `b`.

**2-matrix_divided.py:** function that divides all elements of a matrix.

- Prototype: `def matrix_divided(matrix, div):`
- `matrix` must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`.
- Each row of the `matrix` must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`.
- `div` must be a number (integer or float), otherwise raise a `TypeError` exception with the message `div must be a number`.
- `div` can’t be equal to `0`, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
- All elements of the `matrix` should be divided by `div`, rounded to 2 decimal places.
- Returns a new matrix.

**3-say_my_name:**  prints `My name is <first name> <last name>`

- Prototype: `def say_my_name(first_name, last_name=""):`
`first_name` and `last_name` must be strings otherwise, raise a `TypeError` exception with the message `first_name must be a string or last_name must be a string`.

**tests/0-add_integer.txt:** containts 9 different test cases for the add_integer function.
**tests/2-matrix_divided.txt:** contains 9 different test cases for the matrix_divided function.
**tests/3-say_my_name:** contains 6 different test cases for the say_my_name function.
