from scipy import integrate
import numpy as np


def func(x):
    return x + 2


trapz, v = integrate.quad(func, 1, 2)

print(trapz)
