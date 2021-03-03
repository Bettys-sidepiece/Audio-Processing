"""
This program is meant as a tutorial into using python for data analysis and visualisation
using the libraries numpy, scipy and matplotlib.
"""

import numpy as np
from matplotlib import pyplot as plt

#Generates evenly spread values
t = np.linspace(0, 20, 100)

#Definition of the functions
f_cos = np.cos(t)
f_sin = np.sin(t)

# Plot the function
plt.plot(t, f_cos, "-r", label = " Cosine")
plt.plot(t, f_sin, "-b", label = " Sine")

# Legend location
plt.legend(loc = "lower center")

# Y axis limit
plt.ylim(-1.5, 1.5)
plt.show()

