import matplotlib.pyplot as plt

P_x = [10, 30, 75, 135, 170, 185, 200]
P_y = [10, 75, 50, 55, 25, 95, 45]

plt.figure(figsize=(14, 9))

def plot_scatter_7points():
    for x,y in zip(P_x,P_y):
        label = f"({x},{y})"
        if (x == 30 or x == 135):
            plt.annotate(label, # this is the text
                          (x,y), # these are the coordinates to position the label
                          textcoords="offset points", # how to position the text
                          xytext=(0,10), # distance from text to points (x,y)
                          ha="center") # horizontal alignment (left, right or center)
        elif (x == 75 or x == 170 or x == 200):
            plt.annotate(label,
                          (x,y),
                          textcoords="offset points",
                          xytext=(0,-15),
                          ha="center")
        elif (x == 10 or x == 185):
            plt.annotate(label,
                          (x,y),
                          textcoords="offset points",
                          xytext=(8,0),
                          ha="left")

    plt.grid()

    plt.xlim(0,225)
    plt.ylim(0,100)

    return plt.plot(P_x, P_y, "o--r", markersize = 9)

def Cubic_Bezier_curve_7points(n):
    plot_scatter_7points()

    r_x = []
    r_y = []

    t = []
    t.append(0)

    for i in range(0, n):
        t.append(t[i] + 1/n)

    for i in range(0, len(t)):
        dt = 1-t[i]
        r_x.append(pow(dt,6)*P_x[0] + 6*pow(dt,5)*t[i]*P_x[1] + 15*pow(dt,4)*pow(t[i],2)*P_x[2] + 20*pow(dt,3)*pow(t[i],3)*P_x[3] + 
                   15*pow(dt,2)*pow(t[i],4)*P_x[4] + 6*dt*pow(t[i],5)*P_x[5] + pow(t[i],6)*P_x[6])
        r_y.append(pow(dt,6)*P_y[0] + 6*pow(dt,5)*t[i]*P_y[1] + 15*pow(dt,4)*pow(t[i],2)*P_y[2] + 20*pow(dt,3)*pow(t[i],3)*P_y[3] + 
                   15*pow(dt,2)*pow(t[i],4)*P_y[4] + 6*dt*pow(t[i],5)*P_y[5] + pow(t[i],6)*P_y[6])

    plt.title("Cubic Bezier curve")
    return plt.plot(r_x,r_y,color="blue")

def Catmull_Rom_spline_interpolation(n):
    plot_scatter_7points()

    r_x = []
    r_y = []

    r_x.append(P_x[0])
    r_y.append(P_y[0])

    t = []
    t.append(0)

    for i in range(0, n):
        t.append(t[i] + 1/n)
    for i in range(1, 5):
        for j in range(0, len(t)):
            r_x.append(0.5*(-t[j]*pow(1-t[j],2)*P_x[i-1] + (2-5*t[j]**2+3*pow(t[j],3))*P_x[i] + t[j]*(1+4*t[j]-3*t[j]**2)*P_x[i+1] - t[j]**2*(1-t[j])*P_x[i+2]))
            r_y.append(0.5*(-t[j]*pow(1-t[j],2)*P_y[i-1] + (2-5*t[j]**2+3*pow(t[j],3))*P_y[i] + t[j]*(1+4*t[j]-3*t[j]**2)*P_y[i+1] - t[j]**2*(1-t[j])*P_y[i+2]))
    
    r_x.append(P_x[6])
    r_y.append(P_y[6])

    plt.title("Catmull Rom spline interpolation")
    return plt.plot(r_x,r_y,color="blue")

def Cubic_Beta_Spline_curve(n):
    plot_scatter_7points()

    r_x = []
    r_y = []

    r_x.append(P_x[0])
    r_y.append(P_y[0])

    t = []
    t.append(0)

    for i in range(0, n):
        t.append(t[i] + 1/n)

    for i in range(1, 5):
        for j in range(0, len(t)):
            r_x.append((pow(1-t[j],3)*P_x[i-1] + (3*pow(t[j],3)-6*t[j]**2+4)*P_x[i] + (-3*pow(t[j],3)+3*pow(t[j],2)+3*t[j]+1)*P_x[i+1] + pow(t[j],3)*P_x[i+2])/6)
            r_y.append((pow(1-t[j],3)*P_y[i-1] + (3*pow(t[j],3)-6*t[j]**2+4)*P_y[i] + (-3*pow(t[j],3)+3*pow(t[j],2)+3*t[j]+1)*P_y[i+1] + pow(t[j],3)*P_y[i+2])/6)
  
    r_x.append(P_x[6])
    r_y.append(P_y[6])

    plt.title("Cubic B-Spline curve")
    return plt.plot(r_x,r_y,color="blue")

def Elementary_Beta_spline_curve(n,B1,B2):
    plot_scatter_7points()

    r_x = []
    r_y = []

    r_x.append(P_x[0])
    r_y.append(P_y[0])

    t = []
    t.append(0)

    for i in range(0, n):
        t.append(t[i] + 1/n)

    d = 2*pow(B1,3) + 4*pow(B1,2) + 4*B1 + B2 + 2

    for i in range(1, 5):
        for j in range(0, len(t)):
            b0 = (2*pow(B1,3)*pow(1-t[j],3))/d
            b1 = (2*pow(B1,3)*t[j]*(pow(t[j],2)-3*t[j]+3) + 2*pow(B1,2)*(pow(t[j],3)-3*t[j]+2) + 2*B1*(pow(t[j],3)-3*t[j]+2) + B2*(2*pow(t[j],3)-3*pow(t[j],2)+1))/d
            b2 = (2*pow(B1,2)*pow(t[j],2)*(3-t[j]) + 2*B1*t[j]*(3-pow(t[j],2)) + 2*B2*pow(t[j],2)*(3-2*t[j]) + 2*(1-pow(t[j],3)))/d
            b3 = (2*pow(t[j],3))/d

            r_x.append(b0*P_x[i-1] + b1*P_x[i] + b2*P_x[i+1] + b3*P_x[i+2])
            r_y.append(b0*P_y[i-1] + b1*P_y[i] + b2*P_y[i+1] + b3*P_y[i+2])

    r_x.append(P_x[6])
    r_y.append(P_y[6])

    plt.title("Elementary B-spline curve")
    return plt.plot(r_x,r_y,color="blue")

plt.subplot(2, 2, 1)
Cubic_Bezier_curve_7points(50)

plt.subplot(2, 2, 2)
Catmull_Rom_spline_interpolation(50)

plt.subplot(2, 2, 3)
Cubic_Beta_Spline_curve(10)

plt.subplot(2, 2, 4)
Elementary_Beta_spline_curve(10,1,0.1)

plt.show()