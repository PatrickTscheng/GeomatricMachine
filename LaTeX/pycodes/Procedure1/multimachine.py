from individual import Individual
from buffer import Buffer

class MultiMachine:
    
    MachineNumber = 4

    def __init__(self, Pi, Ri, N, MachineNumber = 4):
        self.MachineNumber = MachineNumber
        self.BufferArray = []
        for i in range(self.MachineNumber-1): self.BufferArray.append(Buffer(N))

        self.Machine = []
        self.Machine.append(Individual(Pi, Ri, None, self.BufferArray[0]))
        for i in range(self.MachineNumber-2):
            self.Machine.append(Individual(Pi, Ri, self.BufferArray[i],self.BufferArray[i+1]))
        self.Machine.append(Individual(Pi, Ri, self.BufferArray[self.MachineNumber-2], None))

    def one_slot(self):
        # step 1: judge if runable
        for i in range(self.MachineNumber): self.Machine[i].b_and_s()
        # step 2: begin run
        M = [0 for i in range(self.MachineNumber)]
        CR, M[0] = self.Machine[0].run_once()
        for i in range(self.MachineNumber-2):
            M[i+1] = self.Machine[i+1].run_once()[1]
        PR, M[self.MachineNumber-1] = self.Machine[self.MachineNumber-1].run_once()
        WIP = []
        ST = []
        BL = []
        for i in range(self.MachineNumber-1): 
            WIP.append(self.BufferArray[i].get_measure())


        for i in range(self.MachineNumber-1):
            if M[i+1] and self.BufferArray[i].check_null():
                ST.append(1)
            else:
                ST.append(0)

        for i in range(self.MachineNumber-2):
            if M[i] and self.BufferArray[i].check_full() and (not M[i+1] or self.BufferArray[i+1].check_full()):
                BL.append(1)
            else:
                BL.append(0)
        if M[self.MachineNumber-2] and self.BufferArray[self.MachineNumber-2].check_full() and (not M[self.MachineNumber-1] ):
            BL.append(1)
        else:
            BL.append(0)
            

        return PR, CR, WIP, ST, BL
