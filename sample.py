from zeta import line
import numpy

# Euler-Mascheroni constant
ec = 0.5772156649


def make_grid(xMarks, yMarks, width, height, n, k):
    """
    Creates a grid of horizontal and vertical lines
    param xMarks: number of vertical lines
    param yMarks: number of horizontal lines
    param width: end point of horizontal lines on the positive x-axis
    param height: end points of the vertical lines on positive and negative y-axis
    param n: number of points on the line
    param k: number of iterations for each point
    """
    lines = []


    i = 0
    # horizontal
    for y in yMarks:
        lines.append(line(y, 0, 1, width, n, k))
        print(i / (len(yMarks) - 1))
        i = i + 1


    for l in lines:
        if l[0][0] < (ec + 0.1):
            l[0][0] = ec

    i = 0
    for x in xMarks:
        lines.append(line(x, 1, -height, height, n, k))
        print(i / (len(xMarks) - 1))
        i = i + 1

    return lines


def flip(lines):
    """
    Produces the "analytic continuation" by flipping the points on the right of
    the critical line to the left
    """
    flipped = []

    for l in lines:
        flippedLine = []
        for x in l:
            flippedLine.append([-1 * (x[0] - ec) + ec, x[1]])

        flipped.append(flippedLine)

    return flipped


def resize(lines, width, height):
    """
    Resizes the lines to fit within the new widths and heights
    """
    maxX = 1
    minX = 1
    maxY = 0
    minY = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            maxX = max(maxX, lines[i][j][0])
            minX = min(minX, lines[i][j][0])
            maxY = max(maxY, lines[i][j][1])
            minY = min(minY, lines[i][j][1])

    print([maxX, minX, maxY, minY])

    fX = width / (maxX - minX)
    fY = height / (maxY - minY)

    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            lines[i][j][0] = (lines[i][j][0] - minX) * fX
            lines[i][j][1] = (lines[i][j][1] - minY) * fY
