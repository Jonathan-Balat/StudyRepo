from numpy import exp


class ActivationClass:

    """REF: https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6"""

    @staticmethod
    def sigmoid(value):
        # return 1/(1+exp(-1*value))
        return 1/(1+exp(-value))

    def delta_sigmoid(self, value):
        s = self.sigmoid(value)
        return s(1-s)

    @staticmethod
    def relu(value):
        return max(0, value)

    def delta_relu(self, value):

        return int(value >= 0)

