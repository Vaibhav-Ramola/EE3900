import numpy as np
import matplotlib.pyplot as plt
# #if using termux
# import subprocess
# import shlex
# #end if


#DTFT
def H(z):
	num = np.polyval([1,0,1],z**(-1))
	den = np.polyval([0.5,1],z**(-1))
	H = num/den
	return H
		


#Input and Output
omega = np.linspace(-3*np.pi,3*np.pi,100)
for i in omega:
	#print(abs(H(np.exp(1j*i))), " ", abs(H(np.exp(0))))
	if abs(abs(H(np.exp(0))) -  abs(H(np.exp(1j*i)))) <= 0.01:
		print("Period of Distcrete Time Fourier Transform is", abs(i))
		break

#subplots
plt.plot(omega, abs(H(np.exp(1j*omega))))
plt.title('Filter Frequency Response')
plt.xlabel('$\omega$')
plt.ylabel('$|H(e^{\jmath\omega})| $')
plt.grid()# minor
plt.show()

# #if using termux
# plt.savefig('../figs/dtft.pdf')
# plt.savefig('../figs/dtft.eps')
# subprocess.run(shlex.split("termux-open ../figs/dtft.pdf"))
# #else
# #plt.show()





