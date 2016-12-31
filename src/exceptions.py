class CalculatorError(RuntimeError):
    def __init__(self, message):
        self.message = message


class EvaluatorError(CalculatorError):
    def __init__(self, message, stack):
        CalculatorError.__init__(self, message)
        self.stack = stack


class NotEnoughArgumentsException(EvaluatorError):
    def __init__(self, message, stack, token):
        EvaluatorError.__init__(self, message, stack)
        self.operator = token


class StackCorruptionException(EvaluatorError):
    def __init__(self, message, stack):
        EvaluatorError.__init__(self, message, stack)
