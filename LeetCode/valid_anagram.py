def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_map = dict()
    for letter in s:
        if letter in s_map:
            s_map[letter] += 1
        else:
            s_map[letter] = 1

    for letter in t:
        if letter in s_map:
            s_map[letter] -= 1
        else:
            return False

    if all(value == 0 for value in s_map.values()):
        return True
    else:
        return False
