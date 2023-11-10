plt.figure(figsize=(14, 4.5))

def oversight_L(X):
    return abs(f(X)-L(X))

plt.subplot(1, 2, 1)
plt.grid()

X_rez  = np.arange(-np.pi/3, np.pi/3+0.01, 0.01)
Y_rez = [oversight_L(x_i) for x_i in X_rez]

plt.plot(X_rez, Y_rez, color = "blue")
plt.subplot(1, 2, 2)
plt.grid()

for i in range(10):
    X_rez = np.arange(x[i], x[i+1]+0.01, 0.01)
    Y_rez = [abs(f(x_i) - S(a,b,c,d,h,i,x_i)) for x_i in X_rez]
    plt.plot(X_rez, Y_rez, color = "red")
