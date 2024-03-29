import random
from buffer import Buffer


class Individual:

    def __init__(self, P: float, R: float,
                 B: Buffer, flag: bool, X_init=False):
        assert (0 <= P and P <= 1) is True
        assert (0 <= R and R <= 1) is True
        self.P = P  # breakdown probability
        self.R = R  # repair probability
        self.x_n = X_init  # state of x false represent down
        self.flag_b_s = False
        # True represents the machine is blockage or stravation
        if flag:  # flag is a special condition control the first(true) and last one(false)
            self.B_b = B  # Buffer backward
            self.B_f = None
        else:
            self.B_b = None
            self.B_f = B  # Buffer forward

    # simulation of a time slot
    # return 1 represent a product return 0 represent no product
    def run_once(self):  # -> int bool

        ONE_PRODUCT = 1
        NO_PRODUCT = 0

        if self.x_n is False:
            if random.random() < self.R:
                self.x_n = True
        else:
            if random.random() < self.P:
                self.x_n = False

        if (self.x_n and (not self.flag_b_s)):
            self.buffer_change()
            return ONE_PRODUCT, self.x_n
        else:
            return NO_PRODUCT, self.x_n

    def blockage(self, B: Buffer) -> bool:
        return B.check_full()

    def starvation(self, B: Buffer) -> bool:
        return B.check_null()

    def b_and_s(self):
        if self.B_f is None:
            self.flag_b_s = self.blockage(self.B_b)
        elif self.B_b is None:
            self.flag_b_s = self.starvation(self.B_f)
        else:
            self.flag_b_s = self.starvation(self.B_f) or self.blockage(self.B_b)

    def buffer_change(self):
        if self.B_f is None:
            self.B_b.add_one()
        elif self.B_b is None:
            self.B_f.take_one()
        else:
            self.B_b.add_one()
            self.B_f.take_one()

    def buffer_get(self):
        if self.B_f is None:
            return self.B_b.get_measure()
        elif self.B_b is None:
            return self.B_f.get_measure()