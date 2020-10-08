# -*- coding: utf-8 -*-
"""
Scripts to generate pictures in lecture-notes-mathematical-analysis LaTeX project.
"""

# --IMPORTS---
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
# from MyScripts import sth

# --CONSTANTS---

# ---FUNCTIONS---


def main():
    limitMultiplication()
    # patrolmen()
    # typesOfDiscontinuity()


def limitMultiplication():
    """ Example 2.2. """
    x = np.linspace(-1, 1, 1000)
    y = x * np.sin(1/x)

    plt.plot(x, y, 'r')
    plt.show()


def patrolmen():
    """ Theorem 2.4. """
    x = np.linspace(-1, 1, 1000)
    f = x**2
    g = -f
    h = f * np.sin(20*1/x)

    size = matplotlib.rcParams['figure.figsize']
    size[0] *= 2
    plt.figure(figsize=size)
    plt.plot(x, f, 'k')
    plt.plot(x, g, 'r')
    plt.plot(x, h, 'b')
    plt.show()


def typesOfDiscontinuity():
    """ Warning following theorem 2.7. """
    x = np.linspace(-1, 1, 10001)
    y = np.sign(x)

    plt.scatter(x, y, c='r', s=1)
    plt.scatter([0], [0], c='r', s=4)
    plt.show()

    y = np.sin(1/x)

    plt.plot(x, y, 'r')
    plt.show()

# ---CLASSES---


# ---MAIN---
if __name__ == '__main__':
    main()
