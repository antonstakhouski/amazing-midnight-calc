from math import sqrt, sin, cos, log10

""" r - right associative (right to left)
    l - left associative (left to right)
"""

BINARY_OPERATORS = {'+': (1, lambda x, y: x + y, 'l'), '-': (1, lambda x, y: x - y, 'l'),
                    '*': (2, lambda x, y: x * y, 'l'), '/': (2, lambda x, y: x / y, 'l'),
                    '^': (4, lambda x, y: x ** y, 'r')}
FUNCTIONS = {'sqr': (9, lambda x: x * x),
             'sqrt': (9, lambda x: sqrt(x)),
             'sin': (9, lambda x: sin(x)),
             'cos': (9, lambda x: cos(x)),
             'abs': (9, lambda x: abs(x)),
             'log10': (9, lambda x: log10(x))}
