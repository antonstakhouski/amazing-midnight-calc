import string
from math import sqrt, sin, cos, log10

BINARY_OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
                    '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}
FUNCTIONS = {'sqr': (9, lambda x: x * x),
             'sqrt': (9, lambda x: sqrt(x)),
             'sin': (9, lambda x: sin(x)),
             'cos': (9, lambda x: cos(x)),
             'abs': (9, lambda x: abs(x)),
             'log10': (9, lambda x: log10(x))}
