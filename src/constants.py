from math import sqrt, sin, cos, log10, e, pi

""" r - right associative (right to left)
    l - left associative (left to right)
    b - binary
    u - unary
"""

OPERATORS = {'+': (1, lambda x, y: x + y, 'l', 'b'), '-': (1, lambda x, y: x - y, 'l', 'b'),
             '*': (2, lambda x, y: x * y, 'l', 'b'), '/': (2, lambda x, y: x / y, 'l', 'b'),
             '//': (2, lambda x, y: x // y, 'l', 'b'),
             '±': (3, lambda x: -x, 'r', 'u'),
             '^': (4, lambda x, y: x ** y, 'r', 'b'),
             'sqr': (9, lambda x: x * x, 'f', 'f'),
             'sqrt': (9, lambda x: sqrt(x), 'f', 'f'),
             'sin': (9, lambda x: sin(x), 'f', 'f'),
             'cos': (9, lambda x: cos(x), 'f', 'f'),
             'abs': (9, lambda x: abs(x), 'l', 'f'),
             'log10': (9, lambda x: log10(x), 'f', 'f')}
FUNCTIONS = {'sqr': (9, lambda x: x * x),
             'sqrt': (9, lambda x: sqrt(x)),
             'sin': (9, lambda x: sin(x)),
             'cos': (9, lambda x: cos(x)),
             'abs': (9, lambda x: abs(x)),
             'log10': (9, lambda x: log10(x))}
CONSTANTS = {'e': e, 'pi': pi}
