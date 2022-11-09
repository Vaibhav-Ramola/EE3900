import numpy as np
from matplotlib import pyplot as plt
import subprocess
import shlex

A = 12
f = 50
t = np.linspace(0, 2/f, 1000)
plt.plot(t, np.abs(A*np.sin(2*np.pi*f*t)))
plt.grid()
plt.xlabel('t')
plt.ylabel('x(t)')
#plt.savefig('../figs/1_1.png')
#subprocess.run(shlex.split('sh gopen.sh ../figs/1_1.png'))
plt.show()
