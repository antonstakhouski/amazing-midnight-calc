from src.constants import OPERATORS


class Evaluator:
    def __init__(self):
        self.stack = []

    def calc(self, polish):
        self.stack = []
        for token in polish:
            #print(self.stack)
            #print(token)
            if token in OPERATORS:
                if OPERATORS[token][3] == 'b':
                    self.binary_operator(token)
                else:
                    self.func_unary_operator(token)
            else:
                # number
                self.stack.append(token)
        return self.stack[0]

    def func_unary_operator(self, token):
        x = self.stack.pop()
        self.stack.append(OPERATORS[token][1](x))

    def binary_operator(self, token):
        y, x = self.stack.pop(), self.stack.pop()
        self.stack.append(OPERATORS[token][1](x, y))
