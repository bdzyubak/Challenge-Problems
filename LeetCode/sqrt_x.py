
# Greedy search
def mySqrt(x: int) -> int:
    if x < 2:
        return x

    c = 2
    c_sq = c ** c
    while c_sq < x:
        c += 1
        c_sq = c * c

    if c_sq == x:

        return c
    else:
        return c - 1



