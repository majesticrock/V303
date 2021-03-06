import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#ohne Rauschen

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b):
    return a*np.cos(x + b)

werte = csv_read("phasenverschiebung.csv")
xdata = np.zeros(13)
ydata = np.zeros(13)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0]) * (np.pi/180)
        ydata[i] = float(values[2])
        i+=1

guess = [25, (np.pi/4)]

x_line = np.linspace(0, np.pi)
plt.plot(xdata, ydata, "r.", label="Messwerte")
popt, pcov = curve_fit(func, xdata, ydata, guess)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)
print(pcov)

plt.xlabel(r"Phasenverschiebung $\Delta\phi$ / rad")
plt.ylabel(r"Amplitude $U$ / V")
plt.legend()
plt.tight_layout()
#plt.show()
plt.savefig("build/plot_phase_rauschen.pdf")