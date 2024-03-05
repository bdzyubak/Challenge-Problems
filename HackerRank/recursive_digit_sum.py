def superDigitBrute(n, k):
    p = ''
    for i in range(k):
        p += n
    # print(p)
    super_digit = calculate_super_digit(p)
    return super_digit


def superDigit(n, k):
    p_digit_sum = sum_digits_once(n) * k
    super_digit = calculate_super_digit(str(p_digit_sum))
    return super_digit


def calculate_super_digit(digit):
    if len(digit) > 1:
        digit_sum = sum_digits_once(digit)
        # print(digit_sum)
        # print(digit_sum)
        digit_sum = calculate_super_digit(str(digit_sum))
    else:
        digit_sum = int(digit)
    return digit_sum


def sum_digits_once(digit):
    digit_sum = 0
    for i in range(len(digit)):
        digit_sum += int(digit[i])
    return digit_sum


if __name__ == '__main__':
    n = '9875'
    k = 4
    assert superDigit(n, k) == 8

    n = '148'
    k = 3
    assert superDigit(n, k) == 3

    n = '9875'
    k = 4
    assert superDigit(n, k) == 8

    n = '123'
    k = 3
    assert superDigit(n, k) == 9
    print('Done')
