import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(9, 6))

def f(x):
    return x*np.tan(x)

x = np.arange(-np.pi/3, np.pi/3, np.pi/15)
x = np.append(x, np.pi/3)
y = [f(x_i) for x_i in x]

plt.plot(x, y, "o", color = "red", markersize = 6)

a,b,c,d,h = [], [], [], [], []

for i in range(0,10):
    a.append(y[i])

for i in range(0,10):
    h.append(x[i+1]-x[i])

C_a = np.array([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [h[1], 2*(h[1]+h[2]), h[2], 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [0.0, h[2], 2*(h[2]+h[3]), h[3], 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [0.0, 0.0, h[3], 2*(h[3]+h[4]), h[4], 0.0, 0.0, 0.0, 0.0, 0.0],
               [0.0, 0.0, 0.0, h[4], 2*(h[4]+h[5]), h[5], 0.0, 0.0, 0.0, 0.0],
               [0.0, 0.0, 0.0, 0.0, h[5], 2*(h[5]+h[6]), h[6], 0.0, 0.0, 0.0],
               [0.0, 0.0, 0.0, 0.0, 0.0, h[6], 2*(h[6]+h[7]), h[7], 0.0, 0.0],
               [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, h[7], 2*(h[7]+h[8]), h[8], 0.0],
               [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, h[8], 2*(h[8]+h[9]), h[9]],
               [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])

C_b = []
C_b.append(0.0)
for i in range(1,9):
    C_b.append(3*(((y[i+1]-y[i])/h[i+1]) - ((y[i]-y[i-1])/h[i])))
C_b.append(0.0)

c = np.linalg.solve(C_a, C_b)

for i in range(0,9):
    b.append((y[i+1]-y[i])/h[i] - h[i]*(c[i+1]+2*c[i])/3)
b.append((y[10]-y[9])/h[9] - 2*h[9]*c[9]/3)

for i in range(0,9):
    d.append((c[i+1]-c[i])/(3*h[i]))
d.append(-c[9]/(3*h[9]))

def S(a,b,c,d,h,i,X):
    return a[i] + b[i]*(X-x[i]) + c[i]*pow((X-x[i]),2) + d[i]*pow((X-x[i]),3)
plt.grid()
plt.axis("equal")

for i in range(10):
    X_rez = np.arange(x[i], x[i+1]+0.01, 0.01)
    Y_rez = [S(a,b,c,d,h,i,x_i) for x_i in X_rez]

    plt.plot(X_rez, Y_rez, color = "blue")
