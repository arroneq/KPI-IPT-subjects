epsilon = 0.001

def func(x):
    return 6*x**5  - 3*x**4 + x**3 + 2*x**2 - 4*x + 2

def derivative_func(x):
    return 30*x**4 - 12*x**3 + 3*x**2 + 4*x - 4

def newton(a,b):
    x = []
    stop = False
    iter = 0

    x.append(a)
    x.append(x[0] - func(x[0])/derivative_func(x[0]))
    if (x[1] > b): 
        x[0]=b
        x[1] = x[0] - func(x[0])/derivative_func(x[0])
    
    if ((abs(x[1]-x[0]) < epsilon) and (abs(func(x[1])) < epsilon)):
        stop = True
        iter = iter + 1
        x_final = x[1]

    i = 1
    while(stop != True):
        x.append(x[i] - func(x[i])/derivative_func(x[i])) 
        if (func(a) * func(x[i+1]) <= 0):
            b = x[i+1]
        if (func(b) * func(x[i+1]) <= 0): 
            a = x[i+1]  

        if ((abs(x[i+1]-x[i]) < epsilon) and (abs(func(x[i+1])) < epsilon)):
            stop = True
            x_final = x[i+1]
        
        i = i + 1
        iter = iter + 1
    
    return round(x_final,8)

print(newton(-1.87,-0.41))