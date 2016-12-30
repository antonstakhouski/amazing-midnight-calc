from src.constants import BINARY_OPERATORS, FUNCTIONS


class ShuntingYard:
    def __init__(self):
        self.stack = []

    def shunting_yard(self, parsed_formula):
        self.stack = []
        for token in parsed_formula:
            # print(token)
            if token in FUNCTIONS:
                yield from self.function_action(token)
            elif token in BINARY_OPERATORS:
                yield from self.binary_operators_action(token)
            elif token == ")":
                yield from self.close_brace_action()
            elif token == "(":
                self.stack.append(token)
                # print(stack)
            else:
                yield token
        while self.stack:
            yield self.stack.pop()

    def binary_operators_action(self, token):
        while self.stack and self.stack[-1] != "(" and self.stack[-1] not in FUNCTIONS and \
                        BINARY_OPERATORS[token][0] <= BINARY_OPERATORS[self.stack[-1]][0]:
            yield self.stack.pop()
        self.stack.append(token)

    def function_action(self, token):
        # print(token)
        # print(stack)
        if token[2] == 'l':
            while self.stack and self.stack[-1] != "(" and FUNCTIONS[token][0] <= FUNCTIONS[self.stack[-1]][0]:
                yield self.stack.pop()
        else:
            while self.stack and self.stack[-1] != "(" and FUNCTIONS[token][0] < FUNCTIONS[self.stack[-1]][0]:
                yield self.stack.pop()
        self.stack.append(token)
        # print(stack)

    def close_brace_action(self):
        while self.stack:
            # print(stack)
            x = self.stack.pop()
            if x == "(":
                if self.stack:
                    x = self.stack[-1]
                    if x in FUNCTIONS:
                        x = self.stack.pop()
                        yield x
                break
            yield x
