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
    return a*x + b

werte = csv_read("photo.csv")
xdata = np.zeros(13)
ydata = np.zeros(13)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = np.log(float(values[0]))
        ydata[i] = np.log(float(values[1])/1000)
        i+=1

#guess = [25, (1/60)]
x_line = np.log(np.linspace(0.1, 1.3))
plt.plot(xdata, ydata, "r.", label="Messwerte")
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)
print(pcov)

plt.xlabel(r"Abstand ln$(r)$ / ln(m)")
plt.ylabel(r"Amplitude ln$(U)$ / ln(mV)")
plt.legend()
plt.tight_layout()
#plt.show()
plt.savefig("build/plot_intensity.pdf")