def count_ways(steps):
    if steps <= 0:
        return 0
    return number_of_ways(steps + 1)


def number_of_ways(steps):
    # Can take one or two steps to reach final steps
    # Return number of ways in which this can be done
    if steps <= 1:
        return steps
    return number_of_ways(steps - 1) + number_of_ways(steps - 2)


if __name__ == '__main__':
    assert count_ways(0) == 0, 'Test did not work for 0 steps'

    assert count_ways(1) == 1, 'Test did not work for 1 steps'

    assert count_ways(2) == 2, 'Test did not work for 2 steps'

    assert count_ways(3) == 3, 'Test did not work for 3 steps'

    assert count_ways(4) == 5, 'Test did not work for 4 steps'

    assert count_ways(5) == 8, 'Test did not work for 5 steps'
