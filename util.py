import matplotlib.pyplot as plt
import numpy as np


def show_stream(width, height, velocity_func, mask_func=None, picture=None):
    """
    Builds StreamPlot for given figure parameters, velocity function and object recognition function

    :param width: plot width limit (negative and positive)
    :param height: plot height limit (negative and positive)
    :param velocity_func: takes point :arg z and returns complex velocity vector in this point
    :param mask_func: takes point :arg z and returns if this point is inside sleek object or not
    :param picture: :class:`artist.Artist` sleek object to be rendered
    :return:
    """

    size = max(width, height)

    y, x = np.mgrid[-height:height:200j, -width:width:200j]
    z = x + 1j * y
    v = velocity_func(z)

    if mask_func is not None:
        v[mask_func(z)] = 0

    vx = np.real(v)
    vy = -np.imag(v)

    plt.figure(figsize=(width, height))
    plt.streamplot(x, y, vx, vy, density=5, minlength=1, arrowsize=5)

    if picture is not None:
        ax = plt.gca()
        ax.add_patch(picture)

    plt.show()
