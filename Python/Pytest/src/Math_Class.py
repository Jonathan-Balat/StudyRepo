from functools import lru_cache


class MathClass(object):

    def fibbonacci_sequence_prototype(self, n):
        if n > 1:
            val = self.fibbonacci_sequence_prototype(n - 1) + self.fibbonacci_sequence_prototype(n - 2)
        elif n > 0:
            val = 1
        else:
            val = 0

        return val

    @lru_cache
    def fibbonacci_sequence_lru(self, n):
        if n > 1:
            val = self.fibbonacci_sequence_lru(n - 1) + self.fibbonacci_sequence_lru(n - 2)
        elif n > 0:
            val = 1
        else:
            val = 0

        return val


if __name__ == '__main__':
    mc = MathClass()

    print(f"Result = {mc.fibbonacci_sequence_prototype(3)}")