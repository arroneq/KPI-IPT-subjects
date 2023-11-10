epsilon = 0.001

def func(x):
    return 6*x**5  - 3*x**4 + x**3 + 2*x**2 - 4*x + 2

def bisection(a,b):
    stop = False
    iter = 0

    while(stop != True):
        c = (a+b)/2
        if (func(a) * func(c) <= 0):
            b = c
        if (func(b) * func(c) <= 0): 
            a = c  

        if (abs(a-b) < epsilon):
            stop = True
            x_final = c
        
        iter = iter + 1
    
    return round(x_final,8)

print(bisection(-1.87,-0.41))