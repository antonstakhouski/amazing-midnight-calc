#!/bin/env python
import unittest

from src.calc import Calculator


class CalcTestSequence(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

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

    def test_epam_advanced(self):
        formula = "10*e^0*log10(.4* -5/-0.1-10) - -abs(-53//10) + -5"
        self.assertEqual(11.0, self.calculator.eval_(formula))

simpleTestSuite = unittest.TestSuite()
simpleTestSuite.addTest(CalcTestSequence('test_sumMulDivSub'))
simpleTestSuite.addTest(CalcTestSequence('test_sqr'))
simpleTestSuite.addTest(CalcTestSequence('test_epam_easy'))
simpleTestSuite.addTest(CalcTestSequence('test_abs'))
# simpleTestSuite.addTest(CalcTestSequence('test_log10'))

if __name__ == '__main__':
    unittest.main()
