import numpy as np
import matplotlib.pyplot as plt

def built_in(a,b,paint,width,equation,alpha):
    if (equation == 'param'):
        t = np.arange(0, 2*np.pi, 0.01)
        x = a*t - b*np.sin(t)
        y = a - b*np.cos(t)

        plt.grid()
        plt.plot(x, y, lw=width, color=paint)

        plt.xlabel('x values')
        plt.ylabel('y values')

        left, right = plt.xlim()
        down, up = plt.ylim()
        plt.xlim(left*alpha, right*alpha)
        plt.ylim(down*alpha, up*alpha)

        return plt.show()

    if (equation == 'polar'):
        phi1 = np.arange(-np.pi/4, np.pi/4, 0.0001)
        phi2 = np.arange(-3*np.pi/4, 5*np.pi/4, 0.0001)
        phi = np.append(phi1,phi2) # whole lemniscate of Bernoulli
        rho = np.sqrt(2*a*a*np.cos(2*phi1)) # or phi2

        plt.polar(phi1, rho, lw=width, color=paint)

        plt.yticks([40, 80, 120])

        left, right = plt.xlim()
        down, up = plt.ylim()
        plt.xlim(left*alpha, right*alpha)
        plt.ylim(down*alpha, up*alpha)

        return plt.show()

def Bresenham(a,b,paint,width,x,y,length,alpha):
    for i in range(length-1):
        x1 = x[i]
        y1 = y[i]
        x2 = x[i+1]
        y2 = y[i+1]

        x_draw = x1
        y_draw = y1

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        s1 = np.sign(x2 - x1)
        s2 = np.sign(y2 - y1)

        if dy > dx:
            dx, dy = dy, dx
            exchange  = 1
        else:
            exchange = 0

        e = 2*dy - dx

        for j in range(int(dx)):
            plt.plot(int(x_draw), int(y_draw), 's', color=paint, markersize=width)

            while (e >= 0):
                if (exchange == 1):
                    x_draw = x_draw + s1
                else:
                    y_draw = y_draw + s2

                e = e - 2*dx

            if (exchange == 1):
                y_draw = y_draw + s2
            else:
                x_draw = x_draw + s1

            e = e + 2*dy
    
    plt.grid()

    plt.xlabel('x values')
    plt.ylabel('y values')

    left, right = plt.xlim()
    down, up = plt.ylim()
    plt.xlim(left*alpha, right*alpha)
    plt.ylim(down*alpha, up*alpha)

    return plt.show()