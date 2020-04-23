from individual import Individual
from buffer import Buffer


class TwoMachine:

    def __init__(self, P1, R1, P2, R2, N):
        self.B1 = Buffer(N)
        self.M1 = Individual(P1, R1, self.B1, True)
        self.M2 = Individual(P2, R2, self.B1, False)

    def one_slot(self):
        # step 1: judge if runable
        self.M1.b_and_s()
        self.M2.b_and_s()
        # step 2: begin run
        CR, M1_s = self.M1.run_once()
        PR, M2_s = self.M2.run_once()
        WIP = self.B1.get_measure()
        if M2_s and self.B1.check_null():
            ST2 = 1
        else:
            ST2 = 0
        if M1_s and (not M2_s) and self.B1.check_full():
            BL1 = 1
        else:
            BL1 = 0
        return PR, CR, WIP, ST2, BL1
