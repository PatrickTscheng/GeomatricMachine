import random


class Individual:

    def __init__(self, Pi: float, Ri: float, n: int, X_init=0):
        assert (0 <= Pi and Pi <= 1) is True
        assert (0 <= Ri and Ri <= 1) is True
        assert (0 == X_init or X_init == 1) is True
        self.Pi = Pi  # breakdown probability
        self.Ri = Ri  # repair probability
        self.n = n  # number of slot
        self.x_n = X_init  # state of x

    def run_once(self) -> int:  # simulation of a time slot
        if self.x_n == 0:
            if random.random() <= self.Ri:
                self.x_n = 1
        else:
            if random.random() <= self.Pi:
                self.x_n = 0
        return self.x_n

    def run_finish(self) -> int:
        i = 0
        while i < self.n:
            self.run_once()
            i += 1
        return self.x_n
