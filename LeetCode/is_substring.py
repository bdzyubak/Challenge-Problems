def isSubsequence(s: str, t: str) -> bool:
    i = 0
    i_s = 0
    while i < len(t) and i_s < len(s):
        if s[i_s] == t[i]:
            i_s += 1
        i += 1
    if i_s < len(s):
        return False
    else:
        return True
