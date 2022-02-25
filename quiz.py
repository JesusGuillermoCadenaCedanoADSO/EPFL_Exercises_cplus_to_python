import numpy as np
tamaño = 3

d = np.empty(0, int)
d = np.full((tamaño, tamaño), 0)
f = np.empty(0, int)

for i in reversed(range(tamaño)):
    d[:, i] += i+1
    a = np.full((tamaño), i + 1)
    f = np.insert(f, 0, a)
f = np.append(f, d.flatten())

print(f)

x = np.array([1, 2, 3])
print(np.r_[np.repeat(x, 3), np.tile(x, 3)])



