import svgwrite
from sample import make_grid
from sample import flip
from sample import resize
import math
import numpy


def make_svg(name, n, k):
    """
    Creates a visualisation of the Riemann-Zeta function
    param name: svg file name
    param n: number of points on each line
    param k: number of iterations for each point
    """

    svg = svgwrite.Drawing(name)

    x = []
    y = []

    x.extend(numpy.arange(0, 0.9, 0.1))
    x.extend(numpy.arange(1.1, 3, 0.1))
    x.extend(numpy.arange(3, 16, 0.5))


    y.extend(numpy.arange(-8, -2, 0.5))
    y.extend(numpy.arange(-2, -0.1, 0.1))
    y.extend(numpy.arange(2, 0.1, -0.1))
    y.extend(numpy.arange(8, 2, -0.5))



    lines = make_grid(x, y, 8, 5, n, k)

    lines.extend(flip(lines))

    resize(lines, 1000, 500)

    for line in lines:
        svg.add(svgwrite.shapes.Polyline(line, stroke='black', fill='none', stroke_width='0.1'))

    svg.save()


make_svg("test.svg", 10000, 100)
