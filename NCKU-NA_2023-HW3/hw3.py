import matplotlib.pyplot as plt
import numpy as np
import sys,time

def main():
    h, t, w0, alpha = user()
    T, XY = rk4(f, 0, t, [1, -alpha], h, w0, alpha)
    if w0**2 - alpha**2 < 0:
        print("w0**2 - alpha**2 < 0,無法計算平方根")
        time.sleep(1)
        sys.exit()
    else:
        actual = np.exp(-alpha * T) * np.cos(T * np.sqrt(w0**2 - alpha**2))
        result(T,XY[:,0],actual)
        sys.exit()

def user():
    while True:
        try:
            h     = float(input('請輸入時間步長大小h : '))
            break
        except ValueError:
            print('請輸入有效數字')
    while True:
        try:
            t     = float(input('請輸入最終時間T : '))
            if t <= 40:
                print('最終時間須大於40')
                continue
            break
        except ValueError:
            print('請輸入有效數字')
    while True:
        try:
            w0    = float(input('請輸入自然頻率w0 : '))
            break
        except  ValueError:
            print('請輸入有效數字')
    while True:
        try:
            alpha = float(input('請輸入阻尼alpha : '))
            break
        except ValueError:
            print('請輸入有效數字')
    return h, t, w0, alpha

def rk4(f, t0, t, xy, h, w0, alpha):
    n = int((t - t0) / h)
    T = np.linspace(t0, t, num=n+1)
    XY= np.zeros((n+1, len(xy)))
    XY[0, :] = xy
    for i in range(n):
        k1 = f(T[i]      , XY[i, :]          ,w0 ,alpha)
        k2 = f(T[i] + h/2, XY[i, :] + h*k1/2 ,w0 ,alpha)
        k3 = f(T[i] + h/2, XY[i, :] + h*k2/2 ,w0 ,alpha)
        k4 = f(T[i] + h  , XY[i, :] + h*k3   ,w0 ,alpha)
        XY[i+1, :] = XY[i, :] + h*(k1 + 2*k2 + 2*k3 + k4)/6
    return T, XY

def f(t, xy, w0, alpha):
    x, y = xy[0], xy[1]
    return np.array([y, -w0**2 * x - 2*alpha * y])

def result(T,rk4_fig,exact_fig):    
    plt.plot(T,rk4_fig,color='r',label='y_rk4')
    plt.plot(T,exact_fig,color='b',linestyle=':',label='y_exact')
    plt.title('RK4 vs Exact')
    plt.legend()
    plt.grid()
    plt.show()
    
main()
