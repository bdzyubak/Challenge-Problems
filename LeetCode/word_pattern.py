def wordPattern(pattern: str, s: str) -> bool:
    words = s.strip().split(' ')

    if len(pattern) != len(words):
        return False

    map = dict()
    for i in range(len(pattern)):
        if pattern[i] in map and words[i] != map[pattern[i]]:
            return False
        elif pattern[i] not in map and words[i] in list(map.values()):
            return False
        elif pattern[i] not in map:
            map[pattern[i]] = words[i]
    return True


pattern = "abba"
s = "dog cat cat dog"
assert wordPattern(pattern, s) is True
