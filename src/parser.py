from src.constants import OPERATORS, CONSTANTS
import string


class Parser:
    def __init__(self):
        self.number = ''
        self.func_or_const = ''
        self.last_token = ''
        self.operator = ''

    def parse(self, formula_string):
        self.number = ''
        self.func_or_const = ''
        self.last_token = ''
        self.operator = ''
        for s in formula_string:
            yield from self.func_or_const_action(s)
            yield from self.number_action(s)
            yield from self.operator_action(s)
        if self.number:
            yield float(self.number)
        if self.func_or_const and self.func_or_const in CONSTANTS:
            yield CONSTANTS[self.func_or_const]

    def operator_action(self, s):
        if s in OPERATORS or s == ")":
            yield from self.operator_closing_brace(s)
        elif self.operator:
            self.last_token = 'operator'
            yield self.operator
            self.operator = ''
        if s == "(":
            if self.last_token == 'number':
                self.last_token = 'operator'
                yield '*'
            yield s

    def operator_closing_brace(self, s):
        if s == '-' and self.last_token != 'number' and self.last_token != ')':
            yield '±'
        elif self.operator and s != '/':
            yield self.operator
            self.operator = ''
        elif s == '/':
            self.last_token = 'operator'
            self.operator += s
        else:
            if s == ')':
                self.last_token = ')'
            else:
                self.last_token = 'operator'
            yield s

    def number_action(self, s):
        if s in string.digits + '.' and not self.func_or_const:
            self.number += s
        elif self.number:
            self.last_token = 'number'
            yield float(self.number)
            self.number = ''

    def func_or_const_action(self, s):
        if s in string.ascii_lowercase:
            # create and grow a string
            self.func_or_const += s
        elif self.func_or_const:
            if self.func_or_const[0] in string.ascii_lowercase and s in string.digits:
                # add digits to string
                self.func_or_const += s
            else:
                yield from self.yield_func_const()

    def yield_func_const(self):
        if self.func_or_const in CONSTANTS:
            self.last_token = 'number'
            yield CONSTANTS[self.func_or_const]
        else:
            self.last_token = 'function'
            yield self.func_or_const
        self.func_or_const = ''
