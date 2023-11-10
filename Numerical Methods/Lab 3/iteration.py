import numpy as np

a = np.array([[5.5, 7.0, 6.0, 5.5],
              [7.0, 10.5, 8.0, 7.0],
              [6.0, 8.0, 10.5, 9.0],
              [5.5, 7.0, 9.0, 10.5]])

length = a[0].size

a_diagonal = np.array([[5.5, 7/11, 17/11, 0.5],
                       [0.0, 35/22, 4/11, 0.0],
                       [0.0, 0.0, 29/14, 0.0],
                       [0.0, 0.0, 3.0, 5.0]])

b = np.array([23.0, 32.0, 33.0, 31.0])

b_diagonal = np.array([45/11, 30/11, 87/35, 8])

c = np.array([[0.0, 0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0]])

d = np.array([0.0, 0.0, 0.0, 0.0])

for i in range(length):
    for j in range(length):
        if (i == j): c[i][j] = 0.0
        else: c[i][j] = -a_diagonal[i][j]/a_diagonal[i][i] 

for i in range(length):
    d[i] = b_diagonal[i]/a_diagonal[i][i]

q = 0
for i in range(length):
    sum = 0
    for j in range(length):
        sum = sum + abs(c[i][j])
    if (sum > q): q = sum

e = 0.0001

x = []
x.append([0.0, 0.0, 0.0, 0.0])

stop = False
i = 0

while (stop != True):
    x.append(np.dot(c,x[i]) + d)
    max = 0
    for j in range(length):
        subtraction = abs(x[i+1][j] - x[i][j])
        if (subtraction > max): max = subtraction

    i = i + 1
    if (q*max/(1-q) < e): stop = True

r = abs(b - np.dot(a,x[len(x)-1]))