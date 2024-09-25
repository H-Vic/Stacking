import numpy as np

def F1(x):
    return np.sum(x**2)

def F2(x):
    return np.sum(np.abs(x)) + np.prod(np.abs(x))

def F3(x):
    dim = len(x)
    o = 0
    for i in range(dim):
        o += np.sum(x[:i+1])**2
    return o

def F4(x):
    return np.max(np.abs(x))

def F5(x):
    dim = len(x)
    return np.sum((np.arange(1, dim+1)) * (x**4)) + np.random.rand()

def F6(x):
    dim = len(x)
    o = 0
    for i in range(dim):
        o += (np.abs(x[i])**(i+2))
    return o

def F7(x):
    dim = len(x)
    o = 0
    for i in range(dim):
        o += (i + 1) * x[i]**2
    return o

def F8(x):
    D = len(x)
    return np.sum(x**2) + np.sum(0.5 * D * (x**2)) + np.sum(0.5 * D * (x**4))

def F9(x):
    dim = len(x)
    return np.sum(0.5 * dim * x**4) + np.random.rand()

def F10(x):
    dim = len(x)
    return np.sum(x**2 - 10 * np.cos(2 * np.pi * x)) + 10 * dim

def F11(x):
    dim = len(x)
    o = 0
    for i in range(dim):
        if np.abs(x[i]) < 0.5:
            o += x[i]**2 - 10 * np.cos(2 * np.pi * x[i]) + 10
        else:
            o += (np.round(2 * x[i]) / 2)**2 - 10 * np.cos(2 * np.pi * np.round(2 * x[i]) / 2) + 10
    return o

def F12(x):
    dim = len(x)
    return -20 * np.exp(-0.2 * np.sqrt(np.sum(x**2) / dim)) - np.exp(np.sum(np.cos(2 * np.pi * x)) / dim) + 20 + np.e

def F13(x):
    dim = len(x)
    return np.sum(x**2) / 4000 - np.prod(np.cos(x / np.sqrt(np.arange(1, dim + 1)))) + 1

def F14(x):
    return np.sum(np.abs(x * np.sin(x) + 0.1 * x))

def F15(x):
    dim = len(x)
    a = 0.5
    b = 3
    kmax = 20

    c1 = a**np.arange(0, kmax + 1)
    c2 = 2 * np.pi * b**np.arange(0, kmax + 1)
    o = 0
    for i in range(dim):
        o += w(x[i], c1, c2)
    return o

def w(x, c1, c2):
    y = np.zeros_like(x)
    for k in range(len(x)):
        y[k] = np.sum(c1 * np.cos(c2 * (x + 0.5))) - k * np.sum(c1 * np.cos(c2 * 0.5))
    return y

def F16(x):
    return 1 - np.cos(2 * np.pi * np.sqrt(np.sum(x**2))) + 0.1 * np.sum(x**2)

def F17(x):
    dim = len(x)
    o = 0
    for i in range(dim - 1):
        o += x[i]**2 + 2 * x[i + 1]**2 - 0.3 * np.cos(2 * np.pi * x[i]) - 0.4 * np.cos(4 * np.pi * x[i + 1]) + 0.7
    return o

def F18(x):
    return (x[1] - (x[0]**2) * 5.1 / (4 * np.pi**2) + 5 / np.pi * x[0] - 6)**2 + 10 * (1 - 1 / (8 * np.pi)) * np.cos(x[0]) + 10

def Functions_details(F):
    d = 10  # Dimension is 10 by default

    function_map = {
        'F1': (F1, -100, 100, d),
        'F2': (F2, -10, 10, d),
        'F3': (F3, -10, 10, d),
        'F4': (F4, -10, 10, d),
        'F5': (F5, -1.28, 1.28, d),
        'F6': (F6, -1, 1, d),
        'F7': (F7, -10, 10, d),
        'F8': (F8, -5, 10, d),
        'F9': (F9, -100, 100, d),
        'F10': (F10, -5.12, 5.12, d),
        'F11': (F11, -5.12, 5.12, d),
        'F12': (F12, -50, 50, d),
        'F13': (F13, -600, 600, d),
        'F14': (F14, -10, 10, d),
        'F15': (F15, -10, 10, d),
        'F16': (F16, -5, 5, d),
        'F17': (F17, -2, 2, d),
        'F18': (F18, [-5, 0], [10, 15], 2)
    }

    return function_map[F]

