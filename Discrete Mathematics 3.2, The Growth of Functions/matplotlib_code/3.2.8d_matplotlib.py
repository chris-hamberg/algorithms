from math import floor, ceil, log
import matplotlib.pyplot as plt
import numpy as np

# Name
name = '3.2.8d'
title = '1'

# Constant witnesses
C, k = 6, 1

# Hypothetical complexity
f = lambda x: ((x**3) + (5 * (log(x)))) / ((x**4) + 1)
ftext = 'f(x) = (x^3 + 5 log x) / (x^4 + 1)'

# Bounding function for f(x)
g = lambda x: 1
gtext = 'g(x) = %s'%title

# Input size
size = 25

# Coordinates for f(x) = y
x = np.array([x for x in range(1, size+1)])
y = np.array([f(x) for x in x])

# Coordinates for g(x)
g_x = np.array([g(x) for x in x])

# k Witness
vert = np.array([y for y in range(floor(y[-1]))])
w = np.array([k for y in vert])

plt.plot(x, y, label=ftext)
plt.plot(x, C*g_x, '--', label=gtext, alpha=0.7)
plt.plot(w, vert, '--', label='k = %d'%k, color='grey', linewidth=1, alpha=0.4)
plt.title('f(x) is O(%s)'%title, loc='center')
plt.legend(loc=10)
plt.grid(linestyle=':', alpha=0.4)
plt.xlabel('Input')
plt.ylabel('Time')
plt.savefig(name+'_plot.jpg')
plt.show()
