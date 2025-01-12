import numpy as np
import matplotlib.pyplot as plt


def verdier_paa_y_aksen(x):
    y = -x**2 - 5
    return y


xaksen = np.linspace(-10, 10, 200)
yaksen = [verdier_paa_y_aksen(x) for x in xaksen]

plt.plot(xaksen, yaksen)
plt.show()
