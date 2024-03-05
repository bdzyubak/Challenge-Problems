import re
import string


def flippingBits(n):
    s = bin(n)[2:]
    t = s.maketrans("01", "10")
    s = s.translate(t)
    s = (32 - len(s)) * "1" + s
    return int(s, 2)


if __name__ == '__main__':
    input = 2147483647
    assert flippingBits(input) == 2147483648

    input = 0
    assert flippingBits(input) == 4294967294

    input = 1
    assert flippingBits(input) == 4294967295
