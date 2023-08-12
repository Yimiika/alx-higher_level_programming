#!/usr/bin/python3

"""This program imports the function `add` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.

The code complies with the pycodestyle style guide (version 2.8.*).
"""

from add_0 import add

a = 1
b = 2

print(f"{a} + {b} = {add(a, b)}")
