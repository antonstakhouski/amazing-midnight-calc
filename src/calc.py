from src.parser import Parser
from src.shunting_yard import ShuntingYard
from src.evaluator import Evaluator
from src.exceptions import NotEnoughArgumentsException, StackCorruptionException


class Calculator:
    def __init__(self):
        self.parser = Parser()
        self.shunting_yard = ShuntingYard()
        self.evaluator = Evaluator()

    def eval_(self, formula):
        try:
            value = self.evaluator.calc(self.shunting_yard.shunting_yard(self.parser.parse(formula)))
        except StackCorruptionException as stackExc:
            print(stackExc.message)
            print("Stack:")
            print(stackExc.stack)
        except NotEnoughArgumentsException as argsExc:
            print(argsExc.message)
            print("Invalid operator: " + argsExc.operator)
            print("Stack:")
            print(argsExc.stack)
        else:
            return value
