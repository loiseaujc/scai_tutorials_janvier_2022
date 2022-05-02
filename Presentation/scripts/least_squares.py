import numpy as np

import matplotlib.pyplot as plt

if __name__ == "__main__":

    x = np.linspace(0.5, 1.5, 24)
    y = 2 * x + 1
    y += 0.15*np.random.randn(y.size)

    data = np.c_[x, y]
    np.savetxt("../data/ls_data.dat", data)

    plt.plot(x, y, 'o')
    plt.show()
