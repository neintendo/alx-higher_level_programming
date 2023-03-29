## 0x05-python-exceptions.

**0-safe_print_list.py:**  prints x elements of a list.

- Prototype: `def safe_print_list(my_list=[], x=0):`.
- `my_list` can contain any type (integer, string, etc.)
- All elements must be printed on the same line followed by a new line.
- `x` represents the number of elements to print.
- `x` can be bigger than the length of my_list.
- Returns the real number of elements printed.

**1-safe_print_integer.py:** prints an integer with `"{:d}".format()`.

- Prototype: `def safe_print_integer(value):`
- `value` can be any type (integer, string, etc.).
- The integer should be printed followed by a new line.
- Returns `True` if `value` has been correctly printed (it means the value is an integer).
- Otherwise, returns `False`.

**2-safe_print_list_integers.py:** prints the first x elements of a list and only integers.

- Prototype: `def safe_print_list_integers(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.).
- All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
- `x` represents the number of elements to access in `my_list`.
- `x` can be bigger than the length of `my_list` - if it’s the case, an exception is expected to occur.
- Returns the real number of integers printed.

**3-safe_print_division.py:**  divides 2 integers and prints the result.

- Prototype: `def safe_print_division(a, b):`
- You can assume that `a` and `b` are integers.
- The result of the division should print on the finally: section preceded by `Inside result:`.
- Returns the value of the division, otherwise: `None`.

**4-list_division.py:**  divides element by element 2 lists.

- Prototype: `def list_division(my_list_1, my_list_2, list_length):`
- `my_list_1` and `my_list_2` can contain any type (integer, string, etc.)
- `list_length` can be bigger than the length of both lists.
- Returns a new list (length = `list_length`) with all divisions.
