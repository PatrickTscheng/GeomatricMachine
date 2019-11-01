from individual import Individual 
P = 0.05
R = 0.2
n = 30
X_init = 1
sum = []
Pr = []
Cr = []
max_range = 1000000
indi = []

for i in range(max_range):
    indi.append(Individual(P,R,n,X_init))

for i in range(n):
    sum.append(0)
    Pr.append(0)
    Cr.append(0)
    for j in range(max_range):
        sum[i] += indi[j].run_once()
    sum[i] = (sum[i]/max_range)
    
str_sum = ''
i = 0
for e in sum:
    str_sum += '(' + str(i+1) + ',' + str(e) + ')\n' 
    i += 1

file = open("result.txt",'w')
file.truncate()
file.write(str_sum)#''.join(str(e) for e in sum ))
file.close()


# if __name__ == '__main__':

# import numpy as np

# # 2-D array: 2 x 3
# two_dim_matrix_one = np.array([[1, 2, 3], [4, 5, 6]])
# # 2-D array: 3 x 2
# two_dim_matrix_two = np.array([[1, 2], [3, 4], [5, 6]])

# two_multi_res = np.dot(two_dim_matrix_one, two_dim_matrix_two)
# print('two_multi_res: %s' %(two_multi_res))

# # 1-D array
# one_dim_vec_one = np.array([1, 2, 3])
# one_dim_vec_two = np.array([4, 5, 6])
# one_result_res = np.dot(one_dim_vec_one, one_dim_vec_two)
# print('one_result_res: %s' %(one_result_res))