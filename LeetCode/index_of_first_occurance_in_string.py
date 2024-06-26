def strStr(haystack: str, needle: str) -> int:
    index = -1
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:(i + len(needle))] == needle:
            index = i
            break
    return index

haystack = 'hello'
needle = 'll'
result = strStr(haystack, needle)
assert result == 2

