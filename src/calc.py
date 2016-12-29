import string
from math import *

BINARY_OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
                    '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}
FUNCTIONS = {'sqr': (9, lambda x: x * x),
             'sqrt': (9, lambda x: sqrt(x)),
             'sin': (9, lambda x: sin(x)),
             'cos': (9, lambda x: cos(x)),
             'abs': (9, lambda x: abs(x)),
             'log10': (9, lambda x: log10(x))}
alphabet = string.ascii_lowercase


def eval_(formula):
    def parse(formula_string):
        number = ''
        function = ''
        for s in formula_string:
            if s in '1234567890.':
                number += s
            elif number:
                yield float(number)
                number = ''

            if s in alphabet:
                function += s
            elif function:
                yield function
                function = ''

            if s in BINARY_OPERATORS or s in "()":
                yield s
        if number:
            yield float(number)

    def shunting_yard(parsed_formula):
        stack = []
        for token in parsed_formula:
            # print(token)
            if token in FUNCTIONS:
                #print(token)
                #print(stack)
                while stack and stack[-1] != "(" and FUNCTIONS[token][0] <= FUNCTIONS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
                #print(stack)
            elif token in BINARY_OPERATORS:
                while stack and stack[-1] != "(" and stack[-1] not in FUNCTIONS and BINARY_OPERATORS[token][0] <= BINARY_OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                while stack:
                    #print(stack)
                    x = stack.pop()
                    if x == "(":
                        if stack:
                            x = stack[-1]
                            if x in FUNCTIONS:
                                x = stack.pop()
                                yield x
                        break
                    yield x
            elif token == "(":
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calc(polish):
        stack = []
        for token in polish:
            #print(stack)
            #print(token)
            if token in FUNCTIONS:
                x = stack.pop()
                stack.append(FUNCTIONS[token][1](x))
            elif token in BINARY_OPERATORS:
                y, x = stack.pop(), stack.pop()
                stack.append(BINARY_OPERATORS[token][1](x, y))
            else:
                stack.append(token)
        return stack[0]

    return calc(shunting_yard(parse(formula)))
