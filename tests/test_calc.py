#!/bin/env python
import unittest
from math import e, pi, log10
import pytest

from src.calc import Calculator, Evaluator, Parser, ShuntingYard
from src.exceptions import NotEnoughArgumentsException, StackCorruptionException


class CalcTestSequence(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        self.parser = Parser()
        self.shunting_yard = ShuntingYard()
        self.evaluator = Evaluator()

    def test_mul(self):
        formula = "2*2"
        self.assertEqual(2*2, self.calculator.eval_(formula))

    def test_sumMulDivSub(self):
        formula = "(2+2*2)/(2+2*2)-5"
        self.assertEqual(eval(formula), self.calculator.eval_(formula))

    def test_sqr(self):
        formula = "sqr(2)"
        self.assertEqual(4.0, self.calculator.eval_(formula))

    def test_epam_easy(self):
        formula = "1*4+3.3/(3 + .3)*3(sqrt(4))/(sin(0) + 1)"
        self.assertEqual(10.0, self.calculator.eval_(formula))

    def test_abs(self):
        formula = "abs(5-10)"
        self.assertEqual(5, self.calculator.eval_(formula))

    def test_log10(self):
        formula = "log10(100)"
        self.assertEqual(2.0, self.calculator.eval_(formula))

    def test_integer_division(self):
        formula = "53//10"
        self.assertEqual(eval(formula), self.calculator.eval_(formula))

    def test_exponentiation(self):
        formula = "10*e^0"
        self.assertEqual(10*e**0, self.calculator.eval_(formula))

    def test_epam_advanced(self):
        formula = "10*e^0*log10(.4* -5/-0.1-10) - -abs(-53//10) + -5"
        self.assertEqual(10*e**0*log10(.4 * -5/-0.1-10) - -abs(-53//10) + -5, self.calculator.eval_(formula))

    def test_constants(self):
        formula = "e*pi"
        self.assertEqual(e * pi, self.calculator.eval_(formula))

    def test_unary_minus(self):
        formula = "-5"
        self.assertEqual(eval(formula), self.calculator.eval_(formula))

    def test_not_existing_operation(self):
        formula = "5 # 4"
        with pytest.raises(StackCorruptionException):
            self.evaluator.calc(self.shunting_yard.shunting_yard(self.parser.parse(formula)))

    def test_NotEnoughArgumentsException_binary(self):
        formula = "5 * "
        with pytest.raises(NotEnoughArgumentsException):
            self.evaluator.calc(self.shunting_yard.shunting_yard(self.parser.parse(formula)))

    def test_NotEnoughArgumentsException_unary(self):
        formula = "-"
        with pytest.raises(NotEnoughArgumentsException):
            self.evaluator.calc(self.shunting_yard.shunting_yard(self.parser.parse(formula)))

    def test_NotEnoughArgumentsException_function(self):
        formula = "sqr()"
        with pytest.raises(NotEnoughArgumentsException):
            self.evaluator.calc(self.shunting_yard.shunting_yard(self.parser.parse(formula)))

simpleTestSuite = unittest.TestSuite()


if __name__ == '__main__':
    unittest.main()
