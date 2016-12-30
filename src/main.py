#!/bin/env python

from src.calc import Calculator

if __name__ == "__main__":
    calculator = Calculator()
    while True:
        input_expression = input("> ")
        print(calculator.eval_(input_expression))
