import sys

"""try:
    print("Hello, My name is", sys.argv[1], end="")
    print(".")
except:
    print("Too few arguments")"""


if len(sys.argv) == 1:
    sys.exit("Too few arguments.")
"""elif len(sys.argv) > 2:
    sys.exit("Too many arguments.")"""

"""
print("Hello, My name is", sys.argv[1], end="")
print(".")"""

for arg in sys.argv[1:-1]:
    print("My name is", arg)