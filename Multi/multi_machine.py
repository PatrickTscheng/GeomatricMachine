from individual import Individual
from buffer import Buffer


class MultiMachine:
    
    MachineNumber = 4

    def __init__(self, Pi, Ri, N, MachineNumber = 4):
        self.MachineNumber = MachineNumber
        self.BufferArray = []
        for i in range(self.MachineNumber-1): self.BufferArray.append(Buffer(N))

        self.Machine = []
        self.Machine.append(Individual(Pi, Ri, self.BufferArray[0], True))
        for i in range(self.MachineNumber-2):
            self.Machine.append(Individual(Pi, Ri, self.BufferArray[i], self.BufferArray[i+1]))
        # self.M2 = Individual(Pi, Ri, self.B1, self.B2)
        # self.M3 = Individual(Pi, Ri, self.B2, self.B3)
        self.Machine.append(Individual(Pi, Ri, self.BufferArray[2], False))

    def one_slot(self):
        # step 1: judge if runable
        for i in range(self.MachineNumber): self.Machine[i].b_and_s()
        # step 2: begin run
        M = [0 for i in range(self.MachineNumber)]
        CR, M[0] = self.Machine[0].run_once()
        for i in range(self.MachineNumber-2):
            M[i+1] = self.Machine[i+1].run_once()[1]
        PR, M[3] = self.Machine[self.MachineNumber-1].run_once()
        WIP = []
        ST = []
        BL = []
        for i in range(self.MachineNumber-1): WIP.append(self.BufferArray[i].get_measure())

        for i in range(self.MachineNumber-1):
            if M[i] and self.BufferArray[i].check_null() is True:
                ST.append(1)
            else:
                ST.append(0)

            if M[i] and (not M[i+1]) and self.BufferArray[i].check_full() is True:
                BL.append(1)
            else:
                BL.append(0)

        return PR, CR, WIP, ST, BL