from src.constants import BINARY_OPERATORS
import string


class Parser:
    def __init__(self):
        self.number = ''
        self.function = ''
        self.last_token = ''

    def parse(self, formula_string):
        self.number = ''
        self.function = ''
        self.last_token = ''
        for s in formula_string:
            yield from self.function_action(s)
            yield from self.number_action(s)
            yield from self.operator_action(s)
        if self.number:
            yield float(self.number)

    def operator_action(self, s):
        if s in BINARY_OPERATORS or s == ")":
            self.last_token = 's'
            yield s
        if s == "(":
            if self.last_token == 'number':
                yield '*'
            yield s

    def number_action(self, s):
        if s in string.digits + '.' and not self.function:
            self.number += s
        elif self.number:
            self.last_token = 'number'
            yield float(self.number)
            self.number = ''

    def function_action(self, s):
        if s in string.ascii_lowercase:
            self.function += s
        elif self.function:
            if self.function[0] in string.ascii_lowercase and s in string.digits:
                self.function += s
            else:
                self.last_token = 'function'
                yield self.function
                self.function = ''
