import re
import string


def birthday(string, day, month):
    number_of_divisions = len(string) - month + 1
    valid_partitions = 0
    for i in range(number_of_divisions):
        piece_sum = sum(string[i:(month + i)])
        if piece_sum == day:
            valid_partitions += 1
    return valid_partitions


if __name__ == '__main__':
    string = [2, 2, 1, 3, 2]
    day = 4
    month = 2
    assert birthday(string, day, month) == 2
