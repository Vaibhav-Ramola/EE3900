import numpy as np
import time
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

def nlgn(n, a): return a*n*np.log2(n)
def nsq(n, a): return a*n*n
def ncb(n, a): return a*(n**3)
def nsqlgn(n, a): return a*n*n*np.log2(n)

def fftmtx(n):
    if (n == 1): return np.array([[1]])
    w = np.exp(-1j*2*np.pi*np.arange(n>>1)/n)
    G = fftmtx(n>>1)
    dg = np.diag(w)@G
    F_l = np.concatenate((G, G), axis=0)
    F_r = np.concatenate((dg, -dg), axis=0)
    F = np.concatenate((F_l, F_r), axis=1)
    Q = np.arange(n)
    F[:,np.concatenate((Q[::2], Q[1::2]))] = F[:,Q]
    return F

tl = []
N = 10
for i in range(10):
    st = time.time()
    X = fftmtx(1<<i)
    tl.append(time.time() - st)

plt.plot(np.arange(10), tl, '.')
x = np.linspace(1, 11, 10)
popt, pcov = curve_fit(nlgn, x, tl)
p1 = nlgn(x, *popt)
plt.plot(np.insert(x, 0, 0), np.insert(p1, 0, 0))
popt, pcov = curve_fit(nsq, x, tl)
p1 = nsq(x, *popt)
plt.plot(np.insert(x, 0, 0), np.insert(p1, 0, 0))
popt, pcov = curve_fit(nsqlgn, x, tl)
p1 = nsqlgn(x, *popt)
plt.plot(np.insert(x, 0, 0), np.insert(p1, 0, 0))
popt, pcov = curve_fit(ncb, x, tl)
p1 = ncb(x, *popt)
plt.plot(np.insert(x, 0, 0), np.insert(p1, 0, 0))
plt.savefig('../../figs/q7/7.14.pdf')
# plt.show()