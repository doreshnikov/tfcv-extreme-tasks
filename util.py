import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors


def static_var(varname, value):
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate


@static_var("STREAM_FIGURES", 0)
def show_stream(width, height, velocity_func, mask_func=None, picture=None, pressure=False):
    """
    Builds velocity StreamPlot and pressure contour plot for given figure parameters, velocity function and object recognition function

    :param width: plot width limit (negative and positive)
    :param height: plot height limit (negative and positive)
    :param velocity_func: takes point :arg z and returns complex velocity vector in this point
    :param mask_func: takes point :arg z and returns if this point is inside sleek object or not
    :param picture: :class:`artist.Artist` sleek object to be rendered
    :return:
    """
    
    plt.figure(show_stream.STREAM_FIGURES)
    show_stream.STREAM_FIGURES += 1

    size = max(width, height)
    velocity_func = np.vectorize(velocity_func)
    mask_func = np.vectorize(mask_func)
    ro = 1

    y, x = np.mgrid[-height:height:200j, -width:width:200j]
    z = x + 1j * y
    v = velocity_func(z)

    if mask_func is not None:
        v[mask_func(z)] = 0

    vmod = np.abs(v)
    p = ro / 2 * (np.amax(vmod) ** 2 - vmod**2)
    minp = np.amin(p)
    maxp = np.amax(p)

    vx = np.real(v)
    vy = -np.imag(v)

    plt.figure(figsize=(width, height))
    plt.streamplot(x, y, vx, vy, density=5, minlength=0.1, arrowsize=5, cmap='plasma', color=vmod)
    if (pressure):
        plt.contourf(x, y, p, np.mgrid[minp:maxp:30j], cmap='bwr')
    if picture is not None:
        ax = plt.gca()
        ax.add_patch(picture)

    plt.show()
