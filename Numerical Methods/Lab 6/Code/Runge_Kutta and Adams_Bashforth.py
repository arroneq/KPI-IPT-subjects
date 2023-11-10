import matplotlib.pyplot as plt
import numpy as np

h = 0.1
move_to = np.pi/2

def f(x,y):
    return (1-x**2)*(y-np.sin(x)/np.cos(x)) + 1/pow(np.cos(x),2)

def define_k(x,y,h):
    k1 = h*f(x,y)
    k2 = h*f(x+0.5*h,y+0.5*k1)
    k3 = h*f(x+0.5*h,y+0.5*k2)
    k4 = h*f(x+h,y+k3)

    return k1,k2,k3,k4

def Runge_Kutta_method(x,n):
    y = [0]
    for i in range(n):
        k1,k2,k3,k4 = define_k(x[i],y[i],h)
        y.append(y[i]+(k1 + 2*k2 + 2*k3 + k4)/6)
    x = np.append(x,move_to)

    return x,y

def Adams_Bashforth_method(x):
    x,y = Runge_Kutta_method(x,3)
    for i in range(3,x.size-1):
        y.append(y[i]+h*(55*f(x[i],y[i]) - 59*f(x[i-1],y[i-1]) + 37*f(x[i-2],y[i-2]) - 9*f(x[i-3],y[i-3]))/24)

    return x,y

x = np.arange(0,move_to,h)
x,y_Runge_Kutta = Runge_Kutta_method(x,x.size)

plt.figure(figsize=(14, 4.5))

plt.subplot(1, 2, 1)
plt.grid()
plt.ylim(0,30)

plt.plot(x,y_Runge_Kutta, color = "blue", label = "approximate")
plt.plot(np.arange(0,move_to,0.01), np.tan(np.arange(0,move_to,0.01)), color = "green", label = "tg(x)")
plt.legend(fontsize = "large")

x,y_Adams_Bashforth = Adams_Bashforth_method(x)

plt.subplot(1, 2, 2)
plt.grid()
plt.ylim(0,30)

plt.plot(x,y_Adams_Bashforth, color = "blue", label = "approximate")
plt.plot(np.arange(0,move_to,0.01), np.tan(np.arange(0,move_to,0.01)), color = "green", label = "tg(x)")
plt.legend(fontsize = "large")
