import numpy as np
from scipy.optimize import minimize

eps = 1e-11

def f(x):
    return x[0] ** 3 - 3 * x[0] * x[1] + x[1] ** 3

def df(x):
    return np.array([
       3 * x[0] ** 2 - 3 * x[1],
       3 * x[1] ** 2 - 3 * x[0],
    ])

def ddf(x):
    return np.array([
       [6 * x[0], -3],
       [-3, 6 * x[1]],
    ])   

def solve(x=[1.1, 1.1]):
    for _ in range(1000):
        x_norm = np.linalg.norm(df(x))
        if x_norm <= eps:
            break
        grad = df(x).reshape(2, 1)
        H_inv = np.linalg.inv(ddf(x))
        dx = -(H_inv @ grad).reshape(-1)
        x += dx
    return x

if __name__ == '__main__':
    x = np.array([0.9, 1.1], dtype=float)

    res = minimize(f, x)
    print(res.x)
    print()

    for _ in range(10):
        print(x, f(x))
        x_norm = np.linalg.norm(df(x))
        if x_norm <= eps:
            break
        grad = df(x).reshape(2, 1)
        H_inv = np.linalg.inv(ddf(x))
        dx = -(H_inv @ grad).reshape(-1)
        print(dx)
        print(dx.shape)
        x += dx

#x = 0.1
#while abs(df(x)) > eps:
#    d = - df(x) / ddf(x)
#    x += d
#
#print(x)
