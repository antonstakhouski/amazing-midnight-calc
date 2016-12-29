#!/bin/env python

from calc import eval_

if __name__ == "__main__":
    while True:
        input_expression = input("> ")
        print(eval_(input_expression))
