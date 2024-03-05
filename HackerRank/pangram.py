import re
import string


def pangrams(s):
    cleaned = re.sub(r'[^a-zA-Z]', '', s.lower())
    unique = list(set(cleaned))
    alphabet = set(string.ascii_lowercase)
    if len(unique) == 27:
        return_string = 'pangram'
    else:
        return_string = 'not pangram'
    return return_string


if __name__ == '__main__':
    s = 'We promptly judged antique ivory buckles for the next prize'
    pangrams(s)
