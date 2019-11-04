import random
from buffer import Buffer


class Individual:

    def __init__(self, Pi: float, Ri: float, X_init=False):
        assert (0 <= Pi and Pi <= 1) is True
        assert (0 <= Ri and Ri <= 1) is True
        self.Pi = Pi  # breakdown probability
        self.Ri = Ri  # repair probability
        self.x_n = X_init  # state of x false represent down
        self.flag_b_s = False  # True represents the machine is blockage or stravation 

    # simulation of a time slot
    # return 1 represent a product return 0 represent no product
    def run_once(self):  # -> int bool
        ONE_PRODUCT = 1
        NO_PRODUCT = 0
        if self.x_n is False:
            if random.random() <= self.Ri:
                self.x_n = True
        else:
            if random.random() <= self.Pi:
                self.x_n = False
        if (self.x_n & (not self.flag_b_s)):
            return ONE_PRODUCT, self.x_n
        else:
            return NO_PRODUCT, self.x_n

    def blockage(self, B: Buffer):
        self.flag_b_s = B.check_full

    def starvation(self, B: Buffer):
        self.flag_b_s = B.check_null

    def b_and_s(self, B1: Buffer, B2: Buffer):
        self.starvation(B1) or self.blockage(B2)
