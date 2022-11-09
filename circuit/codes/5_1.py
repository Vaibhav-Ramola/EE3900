import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
import os

fc = 10

def plot_butter(n):
    b, a = signal.butter(n, fc, analog=True)
    f, h = signal.freqs(b, a, worN = np.logspace(-1, 2, 1000))
    plt.semilogx(f, 20*np.log10(abs(h)))

plot_butter_vec = np.vectorize(plot_butter)
plot_butter_vec([1,2,3,4,5,6])
plt.grid()
plt.yticks(np.arange(-40, 1, 5))
plt.ylim(-40, 0)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.legend(['n = 1', 'n = 2', 'n = 3', 'n = 4', 'n = 5', 'n = 6'])
plt.tight_layout()
# plt.savefig('../figs/5_1.png')
# os.system('sh gopen.sh ../figs/5_1.png')
plt.show()