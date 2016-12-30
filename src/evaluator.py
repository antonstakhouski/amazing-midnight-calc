from src.constants import BINARY_OPERATORS, FUNCTIONS


class Evaluator:
    def __init__(self):
        self.stack = []

    def calc(self, polish):
        self.stack = []
        for token in polish:
            #print(stack)
            #print(token)
            if token in FUNCTIONS:
                x = self.stack.pop()
                self.stack.append(FUNCTIONS[token][1](x))
            elif token in BINARY_OPERATORS:
                y, x = self.stack.pop(), self.stack.pop()
                self.stack.append(BINARY_OPERATORS[token][1](x, y))
            else:
                self.stack.append(token)
        return self.stack[0]
