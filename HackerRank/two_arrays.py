def twoArrays(k, A, B):
    A = sorted(A)
    B = sorted(B)[::-1]
    valid = 'YES'
    for n in range(len(A)):
        if A[n] + B[n] < k:
            valid = 'NO'

    return valid


if __name__ == '__main__':
    A = [1, 0]
    B = [0, 2]
    k = 1
    assert twoArrays(k, A, B) == 'YES'

    A = [2, 1, 3]
    B = [7, 8, 9]
    k = 10
    assert twoArrays(k, A, B) == 'YES'

    A = [1, 2, 2, 1]
    B = [3, 3, 3, 4]
    k = 5
    assert twoArrays(k, A, B) == 'NO'
    print('Done.')
