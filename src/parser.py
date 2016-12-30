from src.constants import BINARY_OPERATORS, alphabet


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
            if s in '1234567890.':
                self.number += s
            elif self.number:
                self.last_token = 'number'
                yield float(self.number)
                self.number = ''

            if s in alphabet:
                self.function += s
            elif self.function:
                self.last_token = 'function'
                yield self.function
                self.function = ''

            if s in BINARY_OPERATORS or s == ")":
                self.last_token = 's'
                yield s
            if s == "(":
                if self.last_token == 'number':
                    yield '*'
                yield s
        if self.number:
            yield float(self.number)
