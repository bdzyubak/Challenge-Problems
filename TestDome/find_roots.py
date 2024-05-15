import numpy as np

def find_roots(a, b, c):
    x1 = (-b + np.sqrt(b**2 - 4*a*c)) / 2 / a
    x2 = (-b - np.sqrt(b ** 2 - 4 * a * c)) / 2 / a
    return (x1, x2)


print(find_roots(2, 10, 8))  # -1, -4; -4, -1