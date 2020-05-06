from multi_machine import MultiMachine

Pi = 0.05  # break down probability 
Ri = 0.2  # repair probability 
N = 5  # Buffer space
n = 150  # slot of time
max_range = 100000
indi = []
PR = [0 for i in range(n)]
CR = [0 for i in range(n)]
WIP = []
ST = []
BL = []

for i in range(max_range):  # initial
    indi.append(MultiMachine(Pi, Ri, N))

for i in range(n):
    WIP.append([0 for j in range(MultiMachine.MachineNumber-1)])
    ST.append([0 for j in range(MultiMachine.MachineNumber-1)])
    BL.append([0 for j in range(MultiMachine.MachineNumber-1)])
    for j in range(max_range):
        pr_t, cr_t, wip_t, st_t, bl_t = indi[j].one_slot()
        PR[i] += pr_t
        CR[i] += cr_t
        for k in range(MultiMachine.MachineNumber-1):
            WIP[i][k] += wip_t[k]
            ST[i][k] += st_t[k]
            BL[i][k] += bl_t[k]
        
    PR[i] = PR[i]/max_range
    CR[i] = CR[i]/max_range
    for k in range(MultiMachine.MachineNumber-1):
            WIP[i][k] = WIP[i][k]/max_range
            ST[i][k] = ST[i][k]/max_range
            BL[i][k] = BL[i][k]/max_range

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

for j in range(3):
    i = 1
    str_out += str(j+1) + 'WIP\n'
    for e in WIP:
        str_out += '(' + str(i) + ',' + str(e[j]) + ')\n'
        i += 1

for j in range(3):
    i = 1
    str_out += str(j+1) + 'ST\n'
    for e in ST:
        str_out += '(' + str(i) + ',' + str(e[j]) + ')\n'
        i += 1

for j in range(3):
    i = 1
    str_out += str(j+1) + 'BL\n'
    for e in BL:
        str_out += '(' + str(i) + ',' + str(e[j]) + ')\n'
        i += 1

file = open("result_sim.txt", 'w')
file.truncate()
file.write(str_out)
file.close()
