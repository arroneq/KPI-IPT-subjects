import matplotlib.pyplot as plt
import numpy as np
import copy

n = 15 # one side dimension of nodes number 

u = [] # initial matrix of states
for i in range(n):
    u.append([0.0 for m in range(n)])

for i in range(1,n-1):
    for j in range(1,n-1):
        u[i][j] = 10.0

dx,dy,dt,a,b,c,k,l = 1,1,1,2,1,-10,0.8,0.5 # all the necessary values  

seconds = 20 # how long will your experiment take?

a1 = 1/dt + (2*l*a/dx**2) + (2*l*b/dy**2) + c*l
a2 = a3 = -(a*l)/dx**2
a4 = a5 = -(b*l)/dy**2

U = [] # matrix to save all the states (copy of an each value)
U.append(copy.deepcopy(u))

t = 0 # let the experiment begin!
while (t < seconds):
    u_a = []
    for i in range(n**2):
        u_a.append([0.0 for m in range(n**2)])

    u_b = []
    for i in range(n**2):
        u_b.append(0.0)

    row = 0
    for i in range(n):
        for j in range(n):
            if (j == 0):
                id = n*i + j
                u_a[row][id] = 1.0
                u_a[row][id+1] = -1.0
                row = row + 1
            elif (i == 0 and j != n-1):
                id = n*i + j
                u_a[row][id] = 1.0
                u_a[row][id+n] = -1/(1+k*dy)
                row = row + 1
            elif (j == n-1):
                id = n*i + j
                u_a[row][id] = 1.0
                u_a[row][id-1] = -1.0
                row = row + 1
            elif (i == n-1 and j != 0 and j != n-1):
                id = n*i + j
                u_a[row][id] = 1.0
                u_a[row][id-n] = -1/(1-k*dy)
                row = row + 1
            else:
                id1 = n*i + j
                id2 = n*i + (j+1)
                id3 = n*i + (j-1)
                id4 = n*(i+1) + j
                id5 = n*(i-1) + j

                u_a[row][id1], u_a[row][id2], u_a[row][id3], u_a[row][id4], u_a[row][id5] = a1, a2, a3, a4, a5
                u_b[row] = u[i][j]/dt + (1-l)*(a*(u[i][j+1]-2*u[i][j]+u[i][j-1])/dx**2 + b*(u[i+1][j]-2*u[i][j]+u[i-1][j])/dy**2 - c*u[i][j])

                row = row + 1

    u_id = np.linalg.solve(u_a, u_b)

    # converting u_id to a matrix
    i,j = 0,0
    for id in range(n**2):
        if (id % n == 0 and id != 0): 
            i = i + 1
            j = 0
            u[i][j] = u_id[id]
            j = j + 1
        else: 
            u[i][j] = u_id[id]
            j = j + 1
    
    U.append(copy.deepcopy(u))
    t = t + 1
# drawing the results
x,y = [], []

number = 1
while (number < n+1):
    for i in range(n):
        x.append(number)
    number = number + 1

number = 1
while (number < n+1):
    for i in range(1,n+1):
        y.append(i)
    number = number + 1

for t in range(seconds):
    z = []
    for i in range(n):
        for j in range(n):
            z.append(U[t][i][j])
    ax = plt.axes(projection="3d")
    ax.scatter(x,y,z, c=z, cmap="viridis", linewidth=0.5)
    plt.show()