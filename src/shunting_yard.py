from src.constants import OPERATORS


class ShuntingYard:
    def __init__(self):
        self.stack = []
        self.FUNCTIONS = []
        for operator in OPERATORS:
            if OPERATORS[operator] == 'f':
                self.FUNCTIONS.append(OPERATORS[operator])

    def shunting_yard(self, parsed_formula):
        self.stack = []
        for token in parsed_formula:
            if token in OPERATORS:
                yield from self.operators_action(token)
            elif token == ")":
                yield from self.close_brace_action()
            elif token == "(":
                self.stack.append(token)
            else:
                # number
                yield token
        while self.stack:
            yield self.stack.pop()

    def operators_action(self, token):
        if OPERATORS[token][2] == 'l':
            yield from self.left_associative(token)
        else:
            yield from self.right_associative(token)
        self.stack.append(token)

    def right_associative(self, token):
        while self.stack and self.stack[-1] != "(" and self.stack[-1] not in self.FUNCTIONS and \
                        OPERATORS[token][0] < OPERATORS[self.stack[-1]][0]:
            yield self.stack.pop()

    def left_associative(self, token):
        while self.stack and self.stack[-1] != "(" and self.stack[-1] not in self.FUNCTIONS and \
                        OPERATORS[token][0] <= OPERATORS[self.stack[-1]][0]:
            yield self.stack.pop()

    def close_brace_action(self):
        # return to opening brace
        while self.stack:
            x = self.stack.pop()
            if x == "(":
                if self.stack:
                    x = self.stack[-1]
                    if x in self.FUNCTIONS:
                        # call function
                        x = self.stack.pop()
                        yield x
                break
            yield x
