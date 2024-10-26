
class MathClass(object):

    def fibbonacci_sequence(self, n):
        if n > 1:
            val = self.fibbonacci_sequence(n - 1) + self.fibbonacci_sequence(n - 2)
        elif n > 0:
            val = 1
        else:
            val = 0

        return val


if __name__ == '__main__':
    mc = MathClass()

    print(f"Result = {mc.fibbonacci_sequence(3)}")