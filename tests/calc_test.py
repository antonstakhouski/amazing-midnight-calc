#!/bin/env python
import unittest

from ..src.calc import eval_


class CalcTestSequence(unittest.TestCase):
    def test_sumMulDivSub(self):
        formula = "(2+2*2)/(2+2*2)-5"
        self.assertEqual(-4.0, eval_(formula))

    def test_sqr(self):
        formula = "sqr(2)"
        self.assertEqual(4.0, eval_(formula))

    def test_epam_easy(self):
        # formula = "1*4+3.3/(3 + .3)*3(sqrt(4))/(sin(0) + 1)"
        formula = "1*4+3.3/(3 + .3)*3*(sqrt(4))/(sin(0) + 1)"
        self.assertEqual(10, eval_(formula))

simpleTestSuite = unittest.TestSuite()
simpleTestSuite.addTest(CalcTestSequence('test_sumMulDivSub'))
simpleTestSuite.addTest(CalcTestSequence('test_sqr'))

if __name__ == '__main__':
    unittest.main()
