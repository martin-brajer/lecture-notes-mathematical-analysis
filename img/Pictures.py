# -*- coding: utf-8 -*-
"""
Scripts to generate pictures in lecture-notes-mathematical-analysis LaTeX project.
"""

# --IMPORTS---
import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
# from MyScripts import sth

# --CONSTANTS---

# ---FUNCTIONS---


def main():
    typesOfDiscontinuity()


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
