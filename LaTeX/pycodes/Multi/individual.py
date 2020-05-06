import random
from buffer import Buffer


class Individual:

    def __init__(self, Pi: float, Ri: float,
                 B_f: Buffer,  B_b: Buffer, X_init=False):
        assert (0 <= Pi and Pi <= 1) is True
        assert (0 <= Ri and Ri <= 1) is True
        self.Pi = Pi  # breakdown probability
        self.Ri = Ri  # repair probability
        self.x_n = X_init  # state of x false represent down
        self.flag_b_s = False
        # True represents the machine is blockage or stravation
        if B_f is  None:  # flag is a special condition control
            self.B_b = B_b  # Buffer backward
            self.B_f = None
        elif B_b is None:
            self.B_b = None
            self.B_f = B_f  # Buffer forward
        else:
            self.B_f = B_f  # Buffer forward
            self.B_b = B_b  # Buffer backward

    # simulation of a time slot
    def run_once(self):  # -> int bool

        ONE_PRODUCT = 1
        NO_PRODUCT = 0

        if self.x_n is False:
            if random.random() < self.Ri:
                self.x_n = True
        else:
            if random.random() < self.Pi:
                self.x_n = False

        if (self.x_n and (not self.flag_b_s)):
            self.buffer_change()
            # print("A",self.flag_b_s,self.x_n)
            return ONE_PRODUCT, self.x_n
        else:
            # print("B",self.flag_b_s,self.x_n)
            return NO_PRODUCT, self.x_n

    def blockage(self, B: Buffer) -> bool:
        return B.check_full()

    def starvation(self, B: Buffer) -> bool:
        return B.check_null()

    def b_and_s(self):
        if self.B_f is None:
            # print("blo")
            self.flag_b_s = self.blockage(self.B_b)
        elif self.B_b is None:
            # print("fail")
            self.flag_b_s = self.starvation(self.B_f)
        else:
            self.flag_b_s = self.starvation(self.B_f) \
                or self.blockage(self.B_b)

    def buffer_change(self):
        if self.B_f is None:
            self.B_b.add_one()
        elif self.B_b is None:
            self.B_f.take_one()
        else:
            self.B_b.add_one()
            self.B_f.take_one()
