def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map = dict()
    for i in range(len(s)):
        if s[i] in map and map[s[i]] != t[i]:
            return False
        elif s[i] not in map and t[i] in list(map.values()):
            return False
        else:
            map[s[i]] = t[i]
    return True