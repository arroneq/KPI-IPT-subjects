Runge_Kutta_error = []
Adams_Bashforth_error = []

for i in range(x.size-1):
    Runge_Kutta_error.append(abs(np.tan(x[i]) - y_Runge_Kutta[i]))
    Adams_Bashforth_error.append(abs(np.tan(x[i]) - y_Adams_Bashforth[i]))

plt.figure(figsize=(14, 4.5))

plt.subplot(1, 2, 1)
plt.grid()
plt.plot(x[:-3], Runge_Kutta_error[:-2], color = "purple")

plt.subplot(1, 2, 2)
plt.grid()
plt.plot(x[:-3], Adams_Bashforth_error[:-2], color = "red")
