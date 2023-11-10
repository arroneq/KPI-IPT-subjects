import numpy as np

A = np.array([[7.0, 0.88, 0.93, 1.21],
              [0.88, 4.16, 1.3, 0.15],
              [0.93, 1.3, 6.44, 2.0],
              [1.21, 0.15, 2.0, 9.0]])

length = A[0].size

def find_ij(A):
    max = -1000

    for i in range(length):
        for j in range(length):
            if (abs(A[i][j]) >= max and i != j): 
                max = abs(A[i][j])
                index_i = i
                index_j = j

    return index_i, index_j

def count_S(A):
    S = 0
    for i in range(length):
        for j in range(length):
            if (i != j): S = S + abs(A[i][j])

    return S 



def count_Sa(A):
    Sa = 0
    for i in range(length):
        for j in range(length):
            Sa = Sa + A[i][j]*A[i][j]

    return Sa 

def count_Snd(A):
    Snd = 0
    for i in range(length):
        for j in range(length):
            if (i != j): Snd = Snd + A[i][j]*A[i][j]

    return Snd 

def count_Sd(A):
    Sd = 0
    for i in range(length):
        Sd = Sd + A[i][i]*A[i][i]

    return Sd

e = 0.00001
stop = False
while(stop != True):
    i,j = find_ij(A)
    m = (2*A[i][j])/(A[i][i] - A[j][j])
    c = np.sqrt(0.5 * (1 + 1/np.sqrt(1 + m*m)))
    s = np.sign(m)*np.sqrt(0.5 * (1 - 1/np.sqrt(1 + m*m)))

    T = np.array([[1.0, 0.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.0],
                  [0.0, 0.0, 0.0, 1.0]])
                  
    T[i][j] = -s
    T[j][i] = s
    T[i][i] = T[j][j] = c

    T_t = T.transpose()

    A = np.dot(T_t,A)
    A = np.dot(A,T)
    A[i][j] = 0

    S = count_S(A)
    if (S <= e): stop = True