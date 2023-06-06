# 0x02. Python Import Modules

**0-add.py:** imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.

**1-calculation.py:** imports functions from the file `calculator_1.py`, does some Maths, and prints the result.

**2-args.py:** prints the number of and the list of its arguments.

**3-infinite_add.py:** prints the result of the addition of all arguments.

**4-hidden_discovery.py:** prints all the names defined by the compiled module `hidden_4.pyc`.

**5-variable_load.py:**  imports the variable `a` from the file `variable_load_5.py` and prints its value.

**100-my_calculator.py:** imports all functions from the file calculator_1.py and handles basic operations.

- If the number of arguments is not 3, the program has to:
  - Print `Usage: ./100-my_calculator.py <a> <operator> <b>` followed with a new line.
  - Exit with the value 1.
- Operator can be:
  - `+` for addition.
  - `-` for subtraction.
  - `*` for multiplication.
  - `/` for division.
- If the operator is not one of the above:
  - Print `Unknown operator. Available operators: +, -, * and /` followed with a new line.
  - Exit with the value 1.
