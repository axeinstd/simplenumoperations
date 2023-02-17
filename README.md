# SIMPLE_NUM_OPERATIONS
This pkg now only can calculate maths expressions.

# NOW IN PYPI! View at https://pypi.org/project/simple-num-operations
**install in terminal**:
 ```terminal
 pip install simple-num-operations
 ```

# v01 use:
  **When u install simple-num-operations, colorama install, too**
  Example program use v01:
  ```python
  from simple_num_operations.v01 import calculate
  from simple_num_operations.exceptions_all import NotMathsExpression
  from colorama import Fore  # additional library (unnecessary)
  while True:
    try:
        print(Fore.LIGHTGREEN_EX + f"{calculate(input('>>> '))}" + Fore.RESET)  # use while cycle and run function
    except NotMathsExpression:  # if input not a math expression
        print(Fore.LIGHTRED_EX + 'Not math expr' + Fore.RESET)
    except ZeroDivisionError:  # if devise by zero
        print(Fore.LIGHTRED_EX + 'Cannot devise by zero' + Fore.RESET)
  ```
# v02 use:
 v02 - very simple way to create a console calculator. In function calculate_simple(expression) embedded many checkers.
 Example to use:
  ```python
from simple_num_operations.v02 import calculate_simple  # importing module

while True: print(calculate_simple(input('>>> ')))  # use while cycle and run function

```

# NOW version 1.1!
