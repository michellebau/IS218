"""Not sure what this is for yet"""

class Calculation:
    """ calculation class """

    def __init__(self,values: tuple):
        """ constructor method """
        ____

class Addition(Calculation):
    """ calculation addition class """
    def get_result(self):
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values