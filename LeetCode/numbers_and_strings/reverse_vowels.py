def reverseVowels(self, s: str) -> str:
    # Y is apparently not a vowel. Though sometimes it is... but it isn't covered by test cases.
    vowels = list()
    for letter in s:
        if letter.lower() in 'aeiou':
            vowels.append(letter)
    vowels = vowels[::-1]

    new_str = ""
    vowel_ind = 0
    for letter in s:
        if letter.lower() in 'aeiou':
            new_str += vowels[vowel_ind]
            vowel_ind += 1
        else:
            new_str += letter
    return new_str