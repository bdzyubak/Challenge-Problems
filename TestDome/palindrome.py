# A palindrome is a word that reads the same backward or forward.
#
# Write a function that checks if a given word is a palindrome.
#
# Character case should be ignored.
#
# For example, is_palindrome("Deleveled") should return True as character case should be ignored, resulting in "deleveled", which is a palindrome since it reads the same backward and forward.


def is_palindrome(word):
    word = word.lower()
    for i in range(len(word) // 2):

        if word[i] != word[-1 - i]:
            return False
    return True


assert is_palindrome('Deleveled') is True

assert is_palindrome('Ciao') is False
