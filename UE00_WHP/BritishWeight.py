__author__ = "Karanbir Guron"
__status__ = "Abgenommen"

class BritishWeight:
    """
    >>> a = BritishWeight(29)
    >>> b = BritishWeight(4)
    >>> print(BritishWeight(14))
    1 st
    >>> print(BritishWeight(3))
    3 lb
    """

    def __init__(self, lb):
        """
        Constructor Class for BritishWeights
        :param lb: Pounds
        """
        if lb < 0:
            raise ArithmeticError("Weight can not be negative")
        self._lb = lb

    def __str__(self):
        """
        Outputs the stones and the pounds
        :return: toString method
        """
        if self.stones == 0:
            return f"{self.pounds} lb"
        elif self.pounds == 0:
            return f"{self.stones} st"
        return f"{self.stones} st {self.pounds} lb"

    @property
    def pounds(self):
        """
        property for lb
        :return: pounds
        """
        return self._lb % 14

    @property
    def stones(self):
        """
        property for stones
        :return: stones
        """
        return self._lb // 14


if __name__ == '__main__':
    a = BritishWeight(27)
    b = BritishWeight(30)
    print(a)
    print(b)
