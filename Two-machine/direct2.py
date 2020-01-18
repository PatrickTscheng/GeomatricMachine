from two_machine import TwoMachine
from probability import Probability

P1 = 0.03  # break down probability machine 1
R1 = 0.18  # repair probability machine 1
P2 = 0.06  # break down probability machine 2
R2 = 0.21  # repair probability machine 2
N = 10  # Buffer space
n = 102  # slot of time
max_range = 1000000
indi = []
PR = []
CR = []
P_f2 = [0 for i in range(n-1)]
R_f2 = [0 for i in range(n-1)]
P_b1 = [0 for i in range(n-1)]
R_b1 = [0 for i in range(n-1)]

for i in range(max_range):  # initial
    indi.append(TwoMachine(P1, R1, P2, R2, N))

for i in range(n):
    PR.append([0 for j in range(max_range)])
    CR.append([0 for j in range(max_range)])
    P_f2_p = Probability(0, 1)
    R_f2_p = Probability(1, 0)
    P_b1_p = Probability(0, 1)
    R_b1_p = Probability(1, 0)
    for j in range(max_range):
        pr_t, cr_t, _, _, _ = indi[j].one_slot()
        PR[i][j] = pr_t
        CR[i][j] = cr_t
        if i > 1:
            P_f2_p.putin(pr_t, PR[i-1][j])
            R_f2_p.putin(pr_t, PR[i-1][j])
            P_b1_p.putin(cr_t, CR[i-1][j])
            R_b1_p.putin(cr_t, CR[i-1][j])
    if i > 1:
        P_f2[i-1] = P_f2_p.get()
        R_f2[i-1] = R_f2_p.get()
        P_b1[i-1] = P_b1_p.get()
        R_b1[i-1] = R_b1_p.get()


str_out = ''
i = 0
str_out += 'P_f2\n'
for e in P_f2:
    str_out += '(' + str(i) + ',' + str(e) + ')\n'
    i += 1

i = 0
str_out += 'R_f2\n'
for e in R_f2:
    str_out += '(' + str(i) + ',' + str(e) + ')\n'
    i += 1

i = 0
str_out += 'P_b1\n'
for e in P_b1:
    str_out += '(' + str(i) + ',' + str(e) + ')\n'
    i += 1

i = 0
str_out += 'R_b1\n'
for e in R_b1:
    str_out += '(' + str(i) + ',' + str(e) + ')\n'
    i += 1

file = open("result_pfb.txt", 'w')
file.truncate()
file.write(str_out)
file.close()
