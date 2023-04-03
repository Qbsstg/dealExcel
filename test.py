from scipy import integrate
import numpy as np


def func(x):
    return x ** 2


x = np.linspace(0, 1, 10)
y = func(x)

trapz = integrate.trapz([100, 99], [1, 2])

print(x)
print(y)
print(trapz)
