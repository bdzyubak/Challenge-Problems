import re
import string


def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res = res + '0'
        else:
            res = res + '1'

    return res


if __name__ == '__main__':
    string_s = '10101'
    string_t = '00101'
    assert strings_xor(string_s, string_t) == '10000'
