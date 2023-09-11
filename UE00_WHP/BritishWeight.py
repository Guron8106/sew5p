class BritishWeight:
    def __init__(self, lb):
        """
        Constructor Class for BritishWeights
        :param lb: Pounds
        """
        if lb < 0:
            raise ArithmeticError("Weight can not be negative")
        self._lb = lb