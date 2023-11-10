import matplotlib.pyplot as plt
import numpy as np

x=[0,100]
y=[0,80]

if (abs(x[1] - x[0]) >= abs(y[1] - y[0])):
    l = abs(x[1] - x[0])
else: l = abs(y[1] - y[0])

dx = (x[1] - x[0]) / l
dy = (y[1] - y[0]) / l

x = x[0] + 0.5 * np.sign(dx)
y = y[0] + 0.5 * np.sign(dy)

i = 1
while (i <= l):
    plt.plot(int(x), int(y), 's', color='red', markersize=5)
    x = x + dx
    y = y + dy
    i = i + 1