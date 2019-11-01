from individual import Individual
from buffer import Buffer


class TwoMachine:

    def __init__(self):
        P1 = 0.03
        R1 = 0.18
        P2 = 0.06
        R2 = 0.21
        N = 10
        self.M1 = Individual(P1, R1)
        self.M2 = Individual(P2, R2)
        self.B1 = Buffer(N)

    def one_slot(self):
        # step 1: judge if runable
        M1.blockage(self.B1)
        M2.starvation(self.B1)
        # step 2: begin run

# 1.git 1)library TrW236 2)ignore 3)latex

# 2.UML 