import math
x1  = -1
x2  = 1.5
tol = 1e-4
def f(x):
    a = math.exp(x)-x-1.0
    return a

while x1 <= x2:
    x = 0.5 * (x1 + x2)
    s = f(x1) * f(x)
    print(x1,f(x1),x2,f(x2),x,f(x));
    if abs(f(x)) <= tol:
        break
    elif s>0 :
        x1 = x
    elif s<0:
        x2 = x


