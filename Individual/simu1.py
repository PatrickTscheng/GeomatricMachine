from individual import Individual
P = 0.05  # break down probability
R = 0.2  # repair probability
n = 40  # numbers of slot
X_init = 1  # initial state of machine
max_range = 1000000  # maxmal quantity of the production lines
sum = []
indi = []

for i in range(max_range):  # initial state of 1
    indi.append(Individual(P, R, n, X_init))

for i in range(n):
    sum.append(0)
    for j in range(max_range):
        sum[i] += indi[j].run_once()
    sum[i] = (sum[i]/max_range)

str_sum = ''
i = 1
for e in sum:
    str_sum += '(' + str(i) + ',' + str(e) + ')\n'
    i += 1

i = 1
for e in sum:
    str_sum += '(' + str(i) + ',' + str(1-e) + ')\n'
    i += 1

# force initial
indi = []
sum = []

for i in range(max_range):  # initial state of 0
    indi.append(Individual(P, R, n))

for i in range(n):
    sum.append(0)
    for j in range(max_range):
        sum[i] += indi[j].run_once()
    sum[i] = (sum[i]/max_range)

i = 1
for e in sum:
    str_sum += '(' + str(i) + ',' + str(e) + ')\n'
    i += 1

i = 1
for e in sum:
    str_sum += '(' + str(i) + ',' + str(1-e) + ')\n'
    i += 1

file = open("result.txt", 'w')
file.truncate()
file.write(str_sum)
file.close()
