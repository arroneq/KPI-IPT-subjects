import numpy as np

a = np.array([[5.5, 7.0, 6.0, 5.5],
              [7.0, 10.5, 8.0, 7.0],
              [6.0, 8.0, 10.5, 9.0],
              [5.5, 7.0, 9.0, 10.5]])

length = a[0].size

b = np.array([23.0, 32.0, 33.0, 31.0])

y = np.array([0.0, 0.0, 0.0, 0.0])

x = np.array([0.0, 0.0, 0.0, 0.0])

t = np.array([[0.0, 0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0]])

t_rev = np.array([[0.0, 0.0, 0.0, 0.0], 
                  [0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0]])

def build_t(a,t):
    # first column is unuque
    d = 0 # index of a diagonal element

    # diagonal element
    t[d][d] = np.sqrt(a[d][d])

    # else elements in the first column 
    for i in range(d+1, length):
        t[i][d] = a[i][d]/t[d][d]

    # general formula for the next diagonal element
    S_row = 0
    for k in range(0, d+1):
        S_row = S_row + t[d+1][k]*t[d+1][k]

    t[d+1][d+1] = np.sqrt(a[d+1][d+1] - S_row)

    for d in range(1, length-1):
        # elements in each column
        for i in range(d+1, length):
            S_cross = 0
            for k in range(0,d):
                S_cross = S_cross + t[i][k]*t[d][k]

            t[i][d] = (a[i][d] - S_cross)/t[d][d]
        # the next diagonal element
        S_row = 0
        for k in range(0, d+1):
            S_row = S_row + t[d+1][k]*t[d+1][k]

        t[d+1][d+1] = np.sqrt(a[d+1][d+1] - S_row)

    return t

t = build_t(a, t)

def build_t_rev(t):
    for i in range(length):
        for j in range(length):
            t_rev[i][j] = t[j][i]
    return t_rev

t_rev = build_t_rev(t)

def find_y(t,b,y):
    y[0]=b[0]/t[0][0]

    for i in range(1, length):
        S_y=0
        for k in range(0, i):
            S_y = S_y + t[i][k]*y[k]
        y[i] = (b[i] - S_y)/t[i][i]

    return y

y = find_y(t,b,y)

def find_x(t_rev,y):
    x[length-1]=y[length-1]/t_rev[length-1][length-1]

    for i in range(length-2, -1, -1):
        S_x=0
        for k in range(length-1, i, -1):
            S_x = S_x + t_rev[i][k]*x[k]
        x[i] = (y[i] - S_x)/t_rev[i][i]

    return x

x = find_x(t_rev,y)

r = abs(b - np.dot(a,x))