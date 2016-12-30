from src.constants import BINARY_OPERATORS, CONSTANTS
import string


class Parser:
    def __init__(self):
        self.number = ''
        self.func_or_const = ''
        self.last_token = ''

    def parse(self, formula_string):
        self.number = ''
        self.func_or_const = ''
        self.last_token = ''
        for s in formula_string:
            yield from self.func_or_const_action(s)
            yield from self.number_action(s)
            yield from self.operator_action(s)
        if self.number:
            yield float(self.number)
        if self.func_or_const and self.func_or_const in CONSTANTS:
            yield CONSTANTS[self.func_or_const]

    def operator_action(self, s):
        if s in BINARY_OPERATORS or s == ")":
            self.last_token = 's'
            yield s
        if s == "(":
            if self.last_token == 'number':
                yield '*'
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
            self.func_or_const += s
        elif self.func_or_const:
            if self.func_or_const[0] in string.ascii_lowercase and s in string.digits:
                self.func_or_const += s
            else:
                self.last_token = 'func_or_const'
                if self.func_or_const in CONSTANTS:
                    yield CONSTANTS[self.func_or_const]
                else:
                    yield self.func_or_const
                self.func_or_const = ''
