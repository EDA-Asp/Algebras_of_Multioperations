class Error(Exception):
    """Base class for other exceptions"""
    pass


class AlgIter(Error):
    """Raised when alg is not closed"""

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class AlgSignature(Error):
    """Raised when alg is not closed"""

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class AlgMetaoperation(Error):
    """Raised when alg is not closed"""

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

