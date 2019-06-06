import matplotlib.pyplot as plt
import numpy as np


# width, height - plot sizes
# velocityFunc should return velocity in complex point
# picture - plot figure
# maskFunc should return true, if given complex point inside area
def showStream(width, height, velocityFunc, picture=None, maskFunc=None):
    Y, X = np.mgrid[-height:height:100j, -width:width:100j]
    Z = X + 1j * Y
    V = velocityFunc(Z)

    if maskFunc is not None:
        V[maskFunc(Z)] = 0

    V_x = np.real(V)
    V_y = -np.imag(V)

    plt.figure(figsize=(width, height))
    plt.streamplot(X, Y, V_x, V_y, density=2.5, minlength=1)

    if picture is not None:
        ax = plt.gca()
        ax.add_patch(picture)

    plt.show()
