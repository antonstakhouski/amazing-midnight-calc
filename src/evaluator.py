from src.constants import OPERATORS, FUNCTIONS


class Evaluator:
    def __init__(self):
        self.stack = []

    def calc(self, polish):
        self.stack = []
        for token in polish:
            #print(self.stack)
            #print(token)
            if token in FUNCTIONS:
                x = self.stack.pop()
                self.stack.append(FUNCTIONS[token][1](x))
            elif token in OPERATORS:
                if OPERATORS[token][3] == 'b':
                    y, x = self.stack.pop(), self.stack.pop()
                    self.stack.append(OPERATORS[token][1](x, y))
                else:
                    x = self.stack.pop()
                    self.stack.append(OPERATORS[token][1](x))
            else:
                self.stack.append(token)
        return self.stack[0]
