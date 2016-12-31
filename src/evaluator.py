from src.constants import OPERATORS
from src.exceptions import NotEnoughArgumentsException, StackCorruptionException


class Evaluator:
    def __init__(self):
        self.stack = []

    def calc(self, polish):
        self.stack = []
        try:
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
            if len(self.stack) != 1:
                raise StackCorruptionException("Stack is corrupted", self.stack)
            else:
                return self.stack[0]
        except StackCorruptionException as stackError:
            raise stackError
        except NotEnoughArgumentsException as argsExc:
            raise argsExc

    def func_unary_operator(self, token):
        if self.stack:
            x = self.stack.pop()
            self.stack.append(OPERATORS[token][1](x))
        else:
            raise NotEnoughArgumentsException("Not enough arguments for unary operator or function", self.stack, token)

    def binary_operator(self, token):
        if len(self.stack) > 1:
            y, x = self.stack.pop(), self.stack.pop()
            self.stack.append(OPERATORS[token][1](x, y))
        else:
            raise NotEnoughArgumentsException("Not enough arguments for binary operator", self.stack, token)
