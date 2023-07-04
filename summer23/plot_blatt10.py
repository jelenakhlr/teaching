# author: Jelena Köhler
# Beispiele zum Plotten - Übungsaufgabe 10.3 der Exp2 im Sommersemster 2023 am KIT
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rc

# mpl setup
mpl.rcParams['lines.markersize'] = 5
# print(mpl.rcParams.keys())

# set fonts and latex
rc('font', **{'family':'serif','serif':['Palatino']})
rc('text', usetex = True)

# set params
R = 20 #Ohm
C = 100E-9 #nF
L = 1E-3 #mH

# set w
w = np.linspace(0,200E3) # in Hz

# define amplitude
def A(w):
    return 1/np.sqrt((1-(w**2 * L * C))**2 + w**2 * R**2 * C**2 )

# plot amplitude
plt.plot(w, A(w), '*', color = 'mediumorchid', label=r'$A(\omega)$')
plt.legend()
plt.xlabel(r"$\omega$ / Hz")
plt.ylabel("amplitude")
plt.grid()
plt.savefig("amp.png", dpi = 300)
plt.show()
plt.close()


# define phi
def phi(w):
    phi = np.arctan((w*R*C)/(1 - (w**2 * L*C)))
    return np.rad2deg(phi) # convert radians to degrees

# plot phi
plt.plot(w, phi(w), '*', color = 'hotpink', label=r'$\phi(\omega)$')
plt.ylim(-75,75)
plt.legend()
plt.xlabel(r"$\omega$ / Hz")
plt.ylabel(r"$\phi$ / deg")
plt.grid()
plt.savefig("phi.png", dpi = 300)
plt.show()
plt.close()
