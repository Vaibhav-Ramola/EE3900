import numpy as np
from scipy import signal, vectorize
from matplotlib import pyplot as plt
import os

fc = 10
eps = 0.5

def plot_cheby1(n):
    b, a = signal.cheby1(n, eps, fc, analog=True)
    f, h = signal.freqs(b, a, worN = np.logspace(-1, 2, 1000))
    lb = 'n = ' + str(n)
    plt.semilogx(f, 20*np.log10(abs(h)), label=lb)
    return

plot_cheby1(1)
plot_cheby1(2)
plot_cheby1(3)
plot_cheby1(4)
plot_cheby1(5)
plot_cheby1(6)
plot_cheby1(7)
plt.grid()
plt.ylim(-2, 0)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.tight_layout()
plt.legend()
# plt.savefig('../figs/5_3.png')
# os.system('sh gopen.sh ../figs/5_3.png')
plt.show()