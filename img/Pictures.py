"""
Scripts to generate pictures in lecture-notes-mathematical-analysis LaTeX project.
"""


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def main():
    mpl.rcParams["savefig.directory"] = __file__

    monotonic()
    # limitMultiplication()
    # patrolmen()
    # typesOfDiscontinuity()

    plt.show()


def monotonic():
    """ Example 2.2. """
    size = mpl.rcParams['figure.figsize']
    size[0] *= 2
    size[1] *= 0.5
    fig, axs = plt.subplots(1, 4, figsize=size)

    x = np.linspace(-1, 1, 1000)
    ys = []
    ys.append(x * 0.7 + 0.3)
    ys.append(1/2/(x + 2) - 0.3)
    _y = - x - 0.5
    _y[x > 0] = -0.5
    ys.append(_y)
    _y = (x**2 - 0.16)*x
    _y[(-0.4 < x) & (x < 0.4)] = 0
    ys.append(_y)

    for ax, y in zip(axs, ys):
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.plot(x, y, 'r')


def limitMultiplication():
    """ Example 2.2. """
    x = np.linspace(-1, 1, 1000)
    y = x * np.sin(1/x)

    plt.plot(x, y, 'r')


def patrolmen():
    """ Theorem 2.4. """
    x = np.linspace(-1, 1, 1000)
    f = x**2
    g = -f
    h = f * np.sin(20*1/x)

    size = mpl.rcParams['figure.figsize']
    size[0] *= 2
    plt.figure(figsize=size)
    plt.plot(x, f, 'k')
    plt.plot(x, g, 'r')
    plt.plot(x, h, 'b')


def typesOfDiscontinuity():
    """ Warning following theorem 2.7. """
    x = np.linspace(-1, 1, 10001)
    y = np.sign(x)

    plt.scatter(x, y, c='r', s=1)
    plt.scatter([0], [0], c='r', s=4)
    plt.show()

    y = np.sin(1/x)
    plt.plot(x, y, 'r')


if __name__ == '__main__':
    main()
