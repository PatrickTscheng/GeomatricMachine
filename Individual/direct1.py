import numpy as np

def exp(A:np.array, n: int):
    A_new = np.copy(A)
    for i in range(n):
        A_new = np.dot(A_new, A)

    return A_new


if __name__ == '__main__':
    R = 0.2
    P = 0.05
    n = 30
    state = np.array([0, 1])
    A1 = np.array([[1-R, P],[R, 1-P]])

    Pr = []
    for i in range(n):
        Pr.append(np.dot(state, exp(A1,i)))

    print (Pr)


