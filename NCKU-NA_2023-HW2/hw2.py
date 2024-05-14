import numpy as np
import matplotlib.pyplot as plt

def lagrange(x, y, xl, yl,num):
    for pt in range(len(xl)):
        k = xl[pt]
        
        idx = np.searchsorted(x, k)
        left_idx = max(0, idx - num)
        right_idx = min(len(x) - 1, idx + num)
        an = 0.0
        #print(k,idx,x[left_idx],x[right_idx])
        for i in range(left_idx, right_idx + 1):
            ai = 1.0
            for j in range(left_idx, right_idx + 1):
                if i != j:
                    ai = ai * (k - x[j]) / (x[i] - x[j])
            an = an + y[i] * ai
        yl[pt] = an


num = int(input('請輸入內插的階數: '))
x, y = np.loadtxt(r"input1.txt", unpack=True)
xl = np.loadtxt(r"input2.txt")
yl = np.zeros(137)

lagrange(x, y, xl, yl,num)


plt.plot(x, y, 'bo', label='original')
plt.plot(xl, yl, 'r+', label='hw2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
