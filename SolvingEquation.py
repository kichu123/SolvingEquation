import numpy as np
from scipy.integrate import quad


def epr(f):
    return 0.5*quad(lambda x:(np.exp(x)-f(x))**2,-1,1)[0]
print(epr(lambda x: 1 + x))

A = np.array([[quad(lambda x, i=i, j=j: x**(i+j), -1, 1)[0] for j in range(3)] for i in range(3)])
rhs = np.array([quad(lambda x, i=i: x**i * np.exp(x), -1, 1)[0] for i in range(3)])
a, b, c = np.linalg.solve(A, rhs)
print(a, b, c)
print(epr(lambda x: a + b*x + c*x**2))

print(epr(np.exp))
