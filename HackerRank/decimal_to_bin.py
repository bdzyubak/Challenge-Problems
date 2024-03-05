def dec_to_bin(n):
    return dec_to_bin_rec(n)


def dec_to_bin_rec(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    bin = dec_to_bin_rec(n // 2) + str(n % 2)
    return bin


def dec2bin(n):  # With leading zeros
    if n < 0:
        return 'Must be a positive integer'
    elif n == 0:
        return '0'
    else:
        return dec2bin(n // 2) + str(n % 2)


if __name__ == "__main__":
    n = 0
    assert dec_to_bin(n) == '0'

    n = 1
    assert dec_to_bin(n) == '1'

    n = 2
    assert dec_to_bin(n) == '10'

    n = 3
    assert dec_to_bin(n) == '11'

    n = 4
    assert dec_to_bin(n) == '100'

    n = 5
    assert dec_to_bin(n) == '101'

    n = 6
    assert dec_to_bin(n) == '110'

    n = 7
    assert dec_to_bin(n) == '111'

    n = 8
    assert dec_to_bin(n) == '1000'

    n = 9
    assert dec_to_bin(n) == '1001'

    n = 10
    assert dec_to_bin(n) == '1010'

    n = 11
    assert dec_to_bin(n) == '1011'

    n = 12
    assert dec_to_bin(n) == '1100'
    print('Done.')
