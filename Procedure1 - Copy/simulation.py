import random
import math
from multiprocessing import Process 
import numpy as np
from multi_machine import MultiMachine

class procedure1:
    

    def __init__(self, MachineNumber = 5):
        self.MachineNumber = MachineNumber

        # production_lines = 1#10000 # production lines
        n = 150  # slot of time
        simulation_num = 100000
        process_all = 20

        # self.calculation( 4, n, simulation_num)
        for i in range(process_all):
            Process(target=self.calculation, args=( i, n, simulation_num)).start()



    def calculation(self, process_num, n, simulation_num):
        # Ri = [random.uniform(0.05, 0.5) for i in range(production_lines)]  # repair probability 
        # # while(Ri == 0.05 or Ri == 0.5):
        # #     Ri = random.uniform(0.05, 0.5)
        # e = [random.uniform(0.6, 0.99) for i in range(production_lines)]
        # # while(e == 0.05 or e == 0.5):
        # #     Ri = random.uniform(0.05, 0.5)
        # Pi =  [Ri[i]/e[i] - Ri[i] for i in range(production_lines)] # break down probability 
        # N = [random.randint(math.ceil(1/Ri[i]), math.ceil(1/Ri[i]*5)) for i in range(production_lines)] # Buffer space
        Pi = 0.05  # break down probability 
        Ri = 0.2  # repair probability 
        N = process_num +1  # Buffer space
        
        indi = []
        PR = [] #[] for i in range(production_lines)]
        CR = [] #[] for i in range(production_lines)]
        WIP = []#[] for i in range(production_lines)]
        ST = []#[] for i in range(production_lines)]
        BL = []#[] for i in range(production_lines)]

        # for i in range(production_lines):  # initial
        #     indi.append(MultiMachine(Pi[i], Ri[i], N[i], self.MachineNumber))

        # for m in range(production_lines):
        for i in range(simulation_num):  # initial
            indi.append(MultiMachine(Pi, Ri, N, self.MachineNumber))

        for i in range(n):
            PR.append(0)
            CR.append(0)
            WIP.append([0 for j in range(self.MachineNumber-1)])
            ST.append([0 for j in range(self.MachineNumber-1)])
            BL.append([0 for j in range(self.MachineNumber-1)])
            

            for j in range(simulation_num):
                
                pr_t, cr_t, wip_t, st_t, bl_t = indi[j].one_slot()
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
            # print(m,i)
        
        # indi = []
 
        # steady paramter PRss and CRss calcualtion
        # steady_sim = 20
        # steady_warmup = 20000
        # steady_cycle = 4000#00
        # PRss = [0 for i in range(production_lines)]
        # CRss = [0 for i in range(production_lines)]
        # for m in range(production_lines):
        #     for i in range(steady_sim):  # initial
        #         indi.append(MultiMachine(Pi, Ri, N, self.MachineNumber))

        #     for i in range(steady_warmup):

        #         for j in range(steady_sim):
                    
        #             indi[j].one_slot()

        #     Prss = np.array([[0 for i in range(steady_sim)] for j in range(steady_cycle)])
        #     Crss = np.array([[0 for i in range(steady_sim)] for j in range(steady_cycle)])

        #     for i in range(steady_cycle):

        #         for j in range(steady_sim):
                    
        #             pr_t, cr_t, __, __, __ = indi[j].one_slot()
        #             Prss[i][j] = pr_t
        #             Crss[i][j] = cr_t
        #             # print(pr_t,cr_t)
        #     PRss = np.mean(Prss).item()
        #     CRss = np.mean(Crss).item()
            
        #     indi = []
        
        # PR_,CR_,WIP_,ST_,BL_ = 


        str_out = ''
        # for m in range(production_lines):
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
                str_out += '(' + str(i) + ',' + str(e[j]) + ')\n'
                i += 1

        for j in range(self.MachineNumber-1):
            i = 1
            str_out += str(j+2) + 'ST\n'
            for e in ST:
                str_out += '(' + str(i) + ',' + str(e[j]) + ')\n'
                i += 1

        for j in range(self.MachineNumber-1):
            i = 1
            str_out += str(j+1) + 'BL\n'
            for e in BL:
                str_out += '(' + str(i) + ',' + str(e[j]) + ')\n'
                i += 1

        # i = 1
        # str_out += 'PRss\n'
        # for e in PRss:
        #     str_out += '(' + str(i) + ',' + str(e) + ')\n'
        #     i += 1

        # i = 1
        # str_out += 'CRss\n'
        # for e in CRss:
        #     str_out += '(' + str(i) + ',' + str(e) + ')\n'
        #     i += 1

        string_name = 'process' + str(process_num) + 'result_sim' + str(self.MachineNumber)
        file = open('{}.txt'.format(string_name), 'w') 
        file.truncate()
        file.write(str_out)
        file.close()

if __name__ == "__main__":
    procedure1()