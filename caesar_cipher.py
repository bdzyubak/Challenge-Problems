def caesar_cipher(s, k):
    # print(s[0])
    # print(shift_letter(s[0],k))
    k = k % 26  # Input sanitization
    s_out = ''
    for letter in s:
        s_out += shift_letter(letter, k)
    return s_out


def shift_letter(letter, k):
    if not letter.isalpha():
        letter_out = letter
        return letter_out

    is_cap, letter = check_capitalization(letter)
    letter_index = ord(letter)
    # print('The letter index is: ' + str(letter_index))
    shifted_index = letter_index + k
    # print('The shifted index is: ' + str(shifted_index))
    # print('The z index is: ' + str(ord('z')))
    if shifted_index > ord('z'):
        shifted_index = ord('a') + shifted_index - ord('z') - 1
    letter_out = chr(shifted_index)
    # print('The shifter letter is: ' + str(letter_out))

    if is_cap:
        letter_out = letter_out.upper()
    return letter_out


def check_capitalization(letter):
    lower_letter = letter.lower()
    if lower_letter != letter:
        is_cap = True
    else:
        is_cap = False
    return is_cap, lower_letter


if __name__ == '__main__':
    assert shift_letter('a', 0) == 'a'

    assert shift_letter('a', 2) == 'c'

    assert shift_letter('x', 3) == 'a'

    s = 'middle-Outz'
    k = 2
    assert caesar_cipher(s, k) == 'okffng-Qwvb'
    print('Done.')

    s = 'www.abc.xy'
