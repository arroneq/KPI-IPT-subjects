import matplotlib.pyplot as plt

plt.figure(figsize=(14, 13.5))

def plot_scatter_4points(P_x,P_y,a,b,c,d):
    i = 1
    for x,y in zip(P_x,P_y):
        label = f"$P_{i}$ ({x},{y})"
        if (i == 1 or i == 4):
            plt.annotate(label, 
                        (x,y),
                        textcoords="offset points",
                        xytext=(0,10),
                        ha="center")
        if (i == 2 or i == 3):
            plt.annotate(label, 
                        (x,y),
                        textcoords="offset points",
                        xytext=(0,-20),
                        ha="center")
    i = i + 1

    plt.grid()
    plt.xlim(-5,200)
    plt.ylim(0,120)

    P_x = [P_x[a], P_x[b], P_x[c], P_x[d]]
    P_y = [P_y[a], P_y[b], P_y[c], P_y[d]]

    return plt.plot(P_x, P_y, 'o--r', markersize = 9)

def Cubic_Bezier_curve_4points(P_x,P_y,n,a,b,c,d):
    plot_scatter_4points(P_x,P_y,a,b,c,d)

    r_x = []
    r_y = []

    t = []
    t.append(0)

    for i in range(0, n):
        t.append(t[i] + 1/n)

    for i in range(0, len(t)):
        dt = 1-t[i]
        r_x.append(pow(dt,3)*P_x[a] + 3*pow(dt,2)*t[i]*P_x[b] + 3*dt*pow(t[i],2)*P_x[c] + pow(t[i],3)*P_x[d])
        r_y.append(pow(dt,3)*P_y[a] + 3*pow(dt,2)*t[i]*P_y[b] + 3*dt*pow(t[i],2)*P_y[c] + pow(t[i],3)*P_y[d])

    plt.title("Cubic Bezier curve")
    return plt.plot(r_x,r_y,color="blue")

P_x = [30, 75, 165, 135]
P_y = [90, 45, 15, 95]

plt.subplot(3, 2, 1)
Cubic_Bezier_curve_4points(P_x,P_y,50,0,1,2,3)

plt.subplot(3, 2, 2)
Cubic_Bezier_curve_4points(P_x,P_y,50,0,1,3,2)

plt.subplot(3, 2, 3)
Cubic_Bezier_curve_4points(P_x,P_y,50,0,2,1,3)

plt.subplot(3, 2, 4)
Cubic_Bezier_curve_4points(P_x,P_y,50,0,2,3,1)

plt.subplot(3, 2, 5)
Cubic_Bezier_curve_4points(P_x,P_y,50,0,3,1,2)

plt.subplot(3, 2, 6)
Cubic_Bezier_curve_4points(P_x,P_y,50,0,3,2,1)

plt.show()