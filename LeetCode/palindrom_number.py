def isPalindrome(x: int) -> bool:
    i = 0
    x = str(x)
    while i < len(x) / 2:
        if x[i] != x[-i - 1]:
            return False
        i += 1
    return True


def isPalindrom(x: int) -> bool:
    x = str(x)

    return x == x[::-1]


# Without converting to string
def isPalindrom(x: int) -> bool:
    if x < 0:
        return False
    if x != 0 and x % 10 == 0: 
        return False

    reversed = 0
    while reversed < x:
        reversed = reversed * 10 + (x % 10)
        x = x // 10
    return True if x == reversed or x == reversed // 10 else False
