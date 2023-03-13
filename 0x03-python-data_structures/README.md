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

**6-print_matrix_integer.py:** prints a matrix of integers.

- Prototype: `def print_matrix_integer(matrix=[[]]):`

**7-add_tuple.py:** adds 2 tuples.

- Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
- Returns a tuple with 2 integers:
- The first element should be the addition of the first element of each argument.
- The second element should be the addition of the second element of each argument.
- If a tuple is smaller than 2, the value 0 will be used for each missing integer
- If a tuple is bigger than 2, only the first 2 integers will be used.

**8-multiple_returns.py:** returns a tuple with the length of a string and its first character.

- Prototype: `def multiple_returns(sentence):`
- If the sentence is empty, the first character should be equal to `None`.

**9-max_integer.py:** finds the biggest integer of a list.

- Prototype: `def max_integer(my_list=[]):`
- If the list is empty, return `None`.

**10-divisible_by_2.py:** finds all multiples of 2 in a list.

- Prototype: `def divisible_by_2(my_list=[]):`
- Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2.

**11-delete_at.py:** deletes the item at a specific position in a list.

- Prototype: `def delete_at(my_list=[], idx=0):`
- If `idx` is negative or out of range, nothing change (returns the same list).
