import math


def counterGame(n):
    print('New game. n is ' + str(n))
    player = 2
    while n > 1:
        if check_power_2(n):
            n = n / 2
        else:
            n = n - reduce_to_power_2(n)
        player += 1
        if player % 2 == 1:
            winner = 'Louise'
        else:
            winner = 'Richard'
        print('The number is now: ' + str(n))
        print('The winner, if stopped, would be: ' + winner)
    if player % 2 == 1:
        winner = 'Louise'
    else:
        winner = 'Richard'
    print(winner)
    return winner


def check_power_2(n):
    if n < 2:
        return False
    log2 = math.log2(n)
    if log2 == math.floor(log2):
        is_power_two = True
    else:
        is_power_two = False
    return is_power_two


def reduce_to_power_2(n):
    if n <= 2:
        return n
    n_reduced_power_two = 2 ** math.floor(math.log2(n))
    return n_reduced_power_two


if __name__ == '__main__':
    n = 2
    assert check_power_2(n) == True

    n = 8
    assert check_power_2(n) == True

    n = 7
    assert check_power_2(n) == False

    n = 0
    assert check_power_2(n) == False

    n = 17
    assert reduce_to_power_2(n) == 16

    n = 3
    assert reduce_to_power_2(n) == 2

    n = 0
    assert reduce_to_power_2(n) == 0

    n = 6
    assert counterGame(n) == 'Richard'

    n = 132
    assert counterGame(n) == 'Louise'
    print('Done')

    n = 1
    assert counterGame(n) == 'Richard'

    n = 1560834904
    assert counterGame(n) == 'Richard'

    n = 1768820483
    assert counterGame(n) == 'Richard'

    n = 1533726144
    assert counterGame(n) == 'Louise'

    n = 1620434450
    assert counterGame(n) == 'Richard'

    n = 1463674015
    assert counterGame(n) == 'Louise'
    print('Done.')
