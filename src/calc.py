from src.parser import Parser
from src.shunting_yard import ShuntingYard
from src.evaluator import Evaluator


class Calculator:
    def __init__(self):
        self.parser = Parser()
        self.shunting_yard = ShuntingYard()
        self.evaluator = Evaluator()

    def eval_(self, formula):
        return self.evaluator.calc(self.shunting_yard.shunting_yard(self.parser.parse(formula)))
    # return calc(shunting_yard(parse(formula)))
