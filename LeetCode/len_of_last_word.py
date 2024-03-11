def lengthOfLastWord(self, s: str) -> int:
    s = s.strip()
    curr = s[-1]
    i = len(s) - 1
    word_len = 0
    while i >= 0 and s[i] != ' ':
        word_len += 1
        i -= 1
    return word_len