import random
import math
from multiprocessing import Process 
import numpy as np
from multi_machine import MultiMachine

class procedure1:
    

    def __init__(self, MachineNumber = 5):
        self.MachineNumber = MachineNumber

        production_lines = 1 # production lines
        n = 300  # slot of time
        simulation_num = 200000
        process_all = 10

        for i in range(process_all):
            Process(target=self.calculation, args=( i, production_lines, n, simulation_num)).start()



    def calculation(self, process_num, production_lines, n, simulation_num):
        Pi = 0.05  # break down probability 
        Ri = 0.2  # repair probability 
        N = process_num +1  # Buffer space
        
        indi = []
        PR = [[] for i in range(production_lines)]
        CR = [[] for i in range(production_lines)]
        WIP = [[] for i in range(production_lines)]
        ST = [[] for i in range(production_lines)]
        BL = [[] for i in range(production_lines)]

        for m in range(production_lines):
            for i in range(simulation_num):  # initial
                indi.append(MultiMachine(Pi, Ri, N, self.MachineNumber))

            for i in range(n):
                PR[m].append(0)
                CR[m].append(0)
                WIP[m].append([0 for j in range(self.MachineNumber-1)])
                ST[m].append([0 for j in range(self.MachineNumber-1)])
                BL[m].append([0 for j in range(self.MachineNumber-1)])
                

                for j in range(simulation_num):
                    
                    pr_t, cr_t, wip_t, st_t, bl_t = indi[j].one_slot()
                    PR[m][i] += pr_t
                    CR[m][i] += cr_t
                    for k in range(self.MachineNumber-1):
                        WIP[m][i][k] += wip_t[k]
                        ST[m][i][k] += st_t[k]
                        BL[m][i][k] += bl_t[k] 
                    
                PR[m][i] = PR[m][i]/simulation_num
                CR[m][i] = CR[m][i]/simulation_num
                for k in range(self.MachineNumber-1):
                        WIP[m][i][k] = WIP[m][i][k]/simulation_num
                        ST[m][i][k] = ST[m][i][k]/simulation_num
                        BL[m][i][k] = BL[m][i][k]/simulation_num
            
            indi = []

        str_out = ''
        for m in range(production_lines):
            i = 1
            str_out += 'PR\n'
            for e in PR[m]:
                str_out += '(' + str(i) + ',' + str(e) + ')\n'
                i += 1

            i = 1
            str_out += 'CR\n'
            for e in CR[m]:
                str_out += '(' + str(i) + ',' + str(e) + ')\n'
                i += 1

            for j in range(self.MachineNumber-1):
                i = 1
                str_out += str(j+1) + 'WIP\n'
                for e in WIP[m]:
                    str_out += '(' + str(i) + ',' + str(e[j]) + ')\n'
                    i += 1

            for j in range(self.MachineNumber-1):
                i = 1
                str_out += str(j+2) + 'ST\n'
                for e in ST[m]:
                    str_out += '(' + str(i) + ',' + str(e[j]) + ')\n'
                    i += 1

            for j in range(self.MachineNumber-1):
                i = 1
                str_out += str(j+1) + 'BL\n'
                for e in BL[m]:
                    str_out += '(' + str(i) + ',' + str(e[j]) + ')\n'
                    i += 1

        string_name = 'process' + str(process_num) + 'result_sim' + str(self.MachineNumber)
        file = open('{}.txt'.format(string_name), 'w') 
        file.truncate()
        file.write(str_out)
        file.close()

if __name__ == "__main__":
    procedure1()