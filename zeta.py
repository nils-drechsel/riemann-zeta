import math
import numpy
from scipy import special

def zeta(s, n):
    """
    Calculates the zeta function value for s, using n iterations
    param s: zeta value
    param n: number of iterations

    """

    p = 1.0 / (1.0 - pow(2, 1.0-s))

    v0 = complex(0, 0)
    for k in range(1, n + 1):
        v0 += pow(-1, k-1) * pow(k, -s)

    v1 = complex(0, 0)
    for k in range(n + 1, 2*n + 1):
        e = 0
        for j in range(k, n + 1):
            e += special.binom(n, j)

        v1 = pow(-1, k-1) * pow(k, -s) * e

    v = p * (v0 + pow(2, -n) * v1)

    return v



def line(x, orientation, start, end, n, k):
    """
    Calculates zeta values for horizontal or vertical lines
    param x: horizontal or vertical fixed location
    param orientation: 0 = vertical line, 1 = horizontal line
    param start: horizontal or vertical start
    param end: horizontal or vertical end
    param n: number of points on the line
    param k: number of iterations for each point
    """
    points = []

    for i in numpy.arange(start, end, (end-start) / float(n)):
        if orientation == 0:
            z = zeta(complex(i, x), k)
        else:
            z = zeta(complex(x, i), k)

        points.append([z.real, z.imag])

    return points
