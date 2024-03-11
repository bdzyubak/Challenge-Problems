def isPalindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return False

    return True


# def isPalindrome(s):
#     s = "".join(filter(lambda x: x in "qwertyuiopasdfghjklzxcvbnm1234567890", list(s.lower())))
#     return s[::-1] == s


s = "A man, a plan, a canal: Panama"
assert isPalindrome(s) is True

s = "race a car"
assert isPalindrome(s) is False

s = " "
assert isPalindrome(s) is True

s = "0P"
assert isPalindrome(s) is False
