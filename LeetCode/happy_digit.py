def isHappy(n: int) -> bool:
    n = str(n)
    sums_seen = list()
    while True:
        squared_digits = list()
        for digit in n:
            squared_digits.append(int(digit) ** 2)
        sum_digits = sum(squared_digits)
        print(f"{squared_digits} {sum_digits}")
        if sum_digits == 1:
            return True
        else:
            n = str(sum_digits)
            if sum_digits in sums_seen:
                return False
            else:
                sums_seen.append(sum_digits)


assert isHappy(19) is True
