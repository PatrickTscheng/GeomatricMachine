from two_machine import TwoMachine

P1 = 0.03  # break down probability machine 1
R1 = 0.18  # repair probability machine 1
P2 = 0.06  # break down probability machine 2
R2 = 0.21  # repair probability machine 2
N = 10  # Buffer space
n = 100  # slot of time
max_range = 1000000
indi = []
PR = []
CR = []
WIP = []
ST2 = []
BL1 = []

for i in range(max_range):  # initial
    indi.append(TwoMachine(P1, R1, P2, R2, N))

for i in range(n):
    PR.append(0.0)
    CR.append(0.0)
    WIP.append(0.0)
    ST2.append(0.0)
    BL1.append(0.0)
    for j in range(max_range):
        pr_t, cr_t, wip_t, st2_t, bl1_t = indi[j].one_slot()
        PR[i] += pr_t
        CR[i] += cr_t
        WIP[i] += wip_t
        ST2[i] += st2_t
        BL1[i] += bl1_t
    PR[i] = PR[i]/max_range
    CR[i] = CR[i]/max_range
    WIP[i] = WIP[i]/max_range
    ST2[i] = ST2[i]/max_range
    BL1[i] = BL1[i]/max_range

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

i = 1
str_out += 'WIP\n'
for e in WIP:
    str_out += '(' + str(i) + ',' + str(e) + ')\n'
    i += 1

i = 1
str_out += 'ST2\n'
for e in ST2:
    str_out += '(' + str(i) + ',' + str(e) + ')\n'
    i += 1

i = 1
str_out += 'BL1\n'
for e in BL1:
    str_out += '(' + str(i) + ',' + str(e) + ')\n'
    i += 1

file = open("result_sim.txt", 'w')
file.truncate()
file.write(str_out)
file.close()
