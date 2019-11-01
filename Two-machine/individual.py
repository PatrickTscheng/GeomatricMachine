import random
from buffer import Buffer


class Individual:


    def __init__(self, Pi: float, Ri: float, X_init = False):
        assert (0 <= Pi and Pi <= 1) == True
        assert (0 <= Ri and Ri <= 1) == True
        self.Pi = Pi  #breakdown probability
        self.Ri = Ri  #repair probability
        self.x_n = X_init  #state of x
        self.flag_b_s = False # True represent the machine is blockage or stravation 


    def run_once(self) -> int:  #simulation of a time slot, return 1 represent a product return 0 represent no product
        ONE_PRODUCT = 1
        NO_PRODUCT = 0
        if self.x_n == False:
            if random.random() <= self.Ri:
                self.x_n = True
        else:
            if random.random() <= self.Pi:
                self.x_n = False
        if (self.x_n & (not self.flag_b_s)):
            return ONE_PRODUCT
        else:
            return NO_PRODUCT

    def b_and_s(self, B1:Buffer, B2:Buffer):
        self.flag_b_s = B1.check_null() or B2.check_full()

    def blockage(self, B:Buffer):
        self.flag_b_s = B.check_full

    def starvation(self, B:Buffer):
        self.flag_b_s = B.check_null
