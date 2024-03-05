# fib_dict = dict()
fib_dict = {2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34}


def check_fibionacci(num):
    isFib = False
    isGreater = False
    n = 0

    while not isFib and not isGreater:
        fib_n = fib_record(n)
        if fib_n == num:
            return True
        if fib_n > num:
            isGreater = True
        n += 1
    return False


# def calc_from_nearest(n):
#     if n in fib_dict: 
#         return fib_dict[n]
#     max_key = max(fib_dict.keys())


def fib(n):
    if n < 0:
        return
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_record(n):
    if n not in fib_dict:
        if n < 0:
            return
        if n <= 1:
            return n
        fib_n = fib(n - 1) + fib(n - 2)
        fib_dict[n] = fib_n
    else:
        fib_n = fib_dict[n]
    return fib_n


if __name__ == '__main__':
    num = 0
    assert check_fibionacci(num) == True

    num = 1
    assert check_fibionacci(num) == True

    num = 2
    assert check_fibionacci(num) == True

    num = 3
    assert check_fibionacci(num) == True

    num = 4
    assert check_fibionacci(num) == False

    num = 5
    assert check_fibionacci(num) == True

    num = 8
    assert check_fibionacci(num) == True

    num = 10
    assert check_fibionacci(num) == False

    num = 13
    assert check_fibionacci(num) == True

    num = 21
    assert check_fibionacci(num) == True

    num = 25
    assert check_fibionacci(num) == False

    num = 34
    assert check_fibionacci(num) == True
    print('Done.')
