def reverseWords( s: str) -> str:
    words = list()
    word = ""
    for i in range(len(s)):
        if s[i] != ' ':
            word += s[i]
        elif s[i] == ' ' and word:
            words.append(word)
            word = ""

    if word:
        words.append(word)

    s_new = ""
    for word in words[::-1]:
        s_new += word + ' '
        print(s_new)

    return s_new[:-1]