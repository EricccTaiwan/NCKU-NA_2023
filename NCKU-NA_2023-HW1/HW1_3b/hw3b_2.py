import math    #3_1

def f(x):                                  
    return (x-1)*(x-4)*(x+2.46)

def newton(xa, tol=1e-5, N0=200): 
    x0 = xa
    for i in range(1, N0):
        f = (x0-1)*(x0-4)*(x0+2.46)
        fd = 3*x0**2 - 5.08*x0 -8.3    
        x = x0 - f/fd
        if abs(x - x0) < tol:
            break
        x0 = x
    return x0, abs(x - x0)

x1 = -10.5 #起點
x2 = 10.5  #終點
n = 11    #分段
dx = (x2 - x1)/(n - 1)  #算delta x
ans =[]             #全部解答的list
results = {}
for i in range(1, n):
    xa = x1 + (i - 1)*dx  #只用左邊的點
    x0, tol = newton(xa)
    results[x0] = tol
    ans.append(x0)  
seen_ints = {}      #建立一個dict
final_result = []   #答案的list
for num in ans:
    int_part = int(num)   #取整數部分
    if int_part not in seen_ints:   #如果int_part是新的數字
        final_result.append(num)    #增加進final_result
        seen_ints[int_part] = True  #看過的整數標示為T
for i in range(len(final_result)):  #用key叫出dict的val
    print('\n','solution=',final_result[i],'tol=',results[final_result[i]])
input()