## 0x03-python-data_structures.

**0-print_list_integer:**  prints all integers of a list.

- Prototype: `def print_list_integer(my_list=[]):`

**1-element_at.py:** retrieves an element from a list like in C.

- Prototype: `def element_at(my_list, idx):`
- If `idx` is negative, the function should return `None`.
- If `idx` is out of range (> of number of element in `my_list`), the function should return `None`.

**2-replace_in_list.py:** replaces an element of a list at a specific position (like in C).

- Prototype: `def replace_in_list(my_list, idx, element):`
- If `idx` is negative, the function should not modify anything, and returns the original list.
- If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list.

**3-print_reversed_list_integer.py:** prints all integers of a list, in reverse order.

- Prototype: `def print_reversed_list_integer(my_list=[]):`

**4-new_in_list.py:** replaces an element in a list at a specific position without modifying the original list (like in C).

- Prototype: `def new_in_list(my_list, idx, element):`
- If `idx` is negative, the function should return a copy of the original `list`.
- If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original `list`.

**5-no_c.py:**  removes all characters c and C from a string.

- Prototype: `def no_c(my_string):`
- The function returns the new string.
