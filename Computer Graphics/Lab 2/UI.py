print('''Hi! Please, choose a curve:
1. x = at-b*sin(x)
   y = a-b*cos(x)
   
2. np.sqrt(2*a*a*np.cos(2*phi))''')

variant = int(input('\nYour answer: '))

if (variant == 1):
    equation = 'param'
if (variant == 2):
    equation = 'polar'

if (equation == 'param'):
    t = np.arange(0, 2*np.pi, 0.3)

    def X(t):
        return a*t - b*np.sin(t)
    def Y(t):
        return a - b*np.cos(t)

    x,y = [],[]
    for i in range(len(t)):
        x.append(X(t[i]))
        y.append(Y(t[i]))

    length = len(t)

if (equation == 'polar'):
    def Up(x):
        return np.sqrt(np.sqrt(pow(a,4) + 4*x**2*a**2) - x**2 - a**2)
    def Down(x):
        return -np.sqrt(np.sqrt(pow(a,4) + 4*x**2*a**2) - x**2 - a**2)

    R_up = np.arange(0, np.sqrt(2)*a, 5)    
    R_down = np.arange(np.sqrt(2)*a, 0, -5)
    L_up = np.arange(0, -np.sqrt(2)*a, -5)
    L_down = np.arange(-np.sqrt(2)*a, 0, 5)

    x_phi1 = np.append(R_up, R_down) 
    x_phi2 = np.append(L_up, L_down)
    x_whole = np.append(x_phi1, x_phi2) # whole lemniscate of Bernoulli
    x = x_phi1 # or x_phi2

    y = []
    for i in range(0, len(x)//2):
        y.append(Up(x[i]))
    for i in range(len(x)//2, len(x)):
        y.append(Down(x[i]))

    length = len(x)
print('''\nNow choose a way to draw this equation:
1. To draw via built-in features of Python
2. To draw via Bresenham algorithm''')

draw = int(input('\nYour answer: '))

# default values (can be changed)
paint = 'blue'
width = 3
alpha = 1

print('\nAnd finally set some necessary values:')
if (equation == 'param'):
    a = int(input('Set a parameter a: '))
    b = int(input('Set a parameter b: '))
if (equation == 'polar'):
    a = int(input('Set a parameter a: '))
    b = 0

if (draw == 1): built_in(a,b,paint,width,equation,alpha)
if (draw == 2): Bresenham(a,b,paint,width,x,y,length,alpha)

def switcher(answer,a,b,draw,paint,width,x,y,length,alpha):
    if (answer == '1'):
        a = int(input('Parameter a: '))
        if (draw == 1): return built_in(a,b,paint,width,equation,alpha)
        if (draw == 2): return Bresenham(a,b,paint,width,x,y,length,alpha)
    if (answer == '2'):
        b = int(input('Parameter b: '))
        if (draw == 1): return built_in(a,b,paint,width,equation,alpha)
        if (draw == 2): return Bresenham(a,b,paint,width,x,y,length,alpha)
    if (answer == '3'):
        paint = input('Color: ')
        if (draw == 1): return built_in(a,b,paint,width,equation,alpha)
        if (draw == 2): return Bresenham(a,b,paint,width,x,y,length,alpha)
    if (answer == '4'):
        width = int(input('Width: '))
        if (draw == 1): return built_in(a,b,paint,width,equation,alpha)
        if (draw == 2): return Bresenham(a,b,paint,width,x,y,length,alpha)
    if (answer == '5'):
        draw = int(input('''A way to draw:
1. To draw via built-in features of Python
2. To draw via Bresenham algorithm 

Your answer: '''))
        if (draw == 1): return built_in(a,b,paint,width,equation,alpha)
        if (draw == 2): return Bresenham(a,b,paint,width,x,y,length,alpha)
    if (answer == '6'):
        alpha = float(input('Scaling coefficient: '))
        if (draw == 1): return built_in(a,b,paint,width,equation,alpha)
        if (draw == 2): return Bresenham(a,b,paint,width,x,y,length,alpha)



stop = False

while (stop != True):
    print('''\nYou can change some values:
1. Change parameter a:
2. Change parameter b:
3. Change a color of a curve
4. Change a width of a curve
5. A way to draw a line
6. Scaling
7. Quit ''')
    answer = input('\nYour answer: ')
    if (answer == '7'): stop = True
    else: switcher(answer,a,b,draw,paint,width,x,y,length,alpha)