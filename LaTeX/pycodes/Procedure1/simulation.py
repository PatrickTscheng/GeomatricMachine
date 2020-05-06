from multiprocessing import Process 
import numpy as np
from multi_machine import MultiMachine

class procedure1:
    

    def __init__(self, MachineNumber = 5):
        self.MachineNumber = MachineNumber
        n = 150  # slot of time
        simulation_num = 100000
        process_all = 20
        for i in range(process_all):
            Process(target=self.calculation, \
                args=( i, n, simulation_num)).start()

    def calculation(self, process_num, n, simulation_num):
        Pi = 0.05  # break down probability 
        Ri = 0.2  # repair probability 
        N = process_num +1  # Buffer space
        
        indi = []
        PR = [] 
        CR = [] 
        WIP = []
        ST = []
        BL = []
        
        for i in range(simulation_num):  # initial
            indi.append(MultiMachine(Pi, Ri, N, \
                self.MachineNumber))

        for i in range(n):
            PR.append(0)
            CR.append(0)
            WIP.append([0 for j in \
                range(self.MachineNumber-1)])
            ST.append([0 for j in range(self.MachineNumber-1)])
            BL.append([0 for j in range(self.MachineNumber-1)])
            

            for j in range(simulation_num):
                
                pr_t, cr_t, wip_t, st_t, bl_t = \
                    indi[j].one_slot()
                PR[i] += pr_t
                CR[i] += cr_t
                for k in range(self.MachineNumber-1):
                    WIP[i][k] += wip_t[k]
                    ST[i][k] += st_t[k]
                    BL[i][k] += bl_t[k] 
                
            PR[i] = PR[i]/simulation_num
            CR[i] = CR[i]/simulation_num
            for k in range(self.MachineNumber-1):
                    WIP[i][k] = WIP[i][k]/simulation_num
                    ST[i][k] = ST[i][k]/simulation_num
                    BL[i][k] = BL[i][k]/simulation_num
        

        str_out = ''
        i = 1
        str_out += 'PR\n'
        for e in PR:
            str_out += '(' + str(i) + ',' + str(e) + ')\n'
            i += 1

        i = 1
        str_out += 'CR\n'
        for e in CR:
            str_out += '(' + str(i) + ',' + str(e) + ')\n'
            i += 1

        for j in range(self.MachineNumber-1):
            i = 1
            str_out += str(j+1) + 'WIP\n'
            for e in WIP:
                str_out += '(' + str(i) + ',' \
                    + str(e[j]) + ')\n'
                i += 1

        for j in range(self.MachineNumber-1):
            i = 1
            str_out += str(j+2) + 'ST\n'
            for e in ST:
                str_out += '(' + str(i) + ',' \
                    + str(e[j]) + ')\n'
                i += 1

        for j in range(self.MachineNumber-1):
            i = 1
            str_out += str(j+1) + 'BL\n'
            for e in BL:
                str_out += '(' + str(i) + ',' \
                    + str(e[j]) + ')\n'
                i += 1

        string_name = 'process' + str(process_num) \
            + 'result_sim' + str(self.MachineNumber)
        file = open('{}.txt'.format(string_name), 'w') 
        file.truncate()
        file.write(str_out)
        file.close()

if __name__ == "__main__":
    procedure1()