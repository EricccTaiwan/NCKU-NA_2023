import math       
def f(x):                                  
    return math.exp(x)-x-1       #eq2_2
def newton(xa,tol = 1e-5,N0=200): 
    x0=xa
    for i in range(1,N0):        #老師的演算法
        f = math.exp(x0)-x0-1    #eq2_2
        fd = math.exp(x0)-1      #微分
        x = x0-f/fd
        if (abs(x-x0) < tol):
            break;
        i = i+1
        x0 = x
    print("solution:",x0,'tol:',abs(x-x0))
      
x1=-5.5 #起點
x2=5.5  #終點
n=11    #分段
dx=(x2-x1)/(n-1)  #算delta x

for i in range(1,n):
    xa=x1+(i-1)*dx
    xb=x1+i*dx
    if f(xa)*f(xb)>0:
        print('no root between',xa,'and',xb)
    if f(xa)==0:
        print('root=',xa,'error=',f(xa))   
    if f(xa)*f(xb)<0:
        print('have root between',xa,'and',xb)
        newton(xa)   
  
input()

