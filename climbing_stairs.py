from sympy import N


def climb_stairs_recursive(stairs):
    if stairs <= 2:
        return stairs
    ways_after_taking_one_step = climb_stairs_recursive(stairs - 1)
    ways_after_taking_two_steps = climb_stairs_recursive(stairs - 2)
    return ways_after_taking_one_step + ways_after_taking_two_steps


def climb_stairs_iterative(stairs):
    if stairs <= 2:
        return stairs

    two_back = 1  # Seed with ways to climb single stair
    one_back = 2  # Seed with ways to climb two stairs
    for i in range(3, stairs + 1):
        n_ways = two_back + one_back
        two_back = one_back
        one_back = n_ways
    return n_ways


if __name__ == '__main__':
    print('Test iterative solution.')
    stairs = 1
    assert climb_stairs_iterative(stairs) == 1

    stairs = 2
    assert climb_stairs_iterative(stairs) == 2

    stairs = 3
    assert climb_stairs_iterative(stairs) == 3

    stairs = 4
    assert climb_stairs_iterative(stairs) == 5  # [1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2]

    stairs = 10
    assert climb_stairs_iterative(stairs) == 89  # [1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2]
    print('Done testing iterative.')

    print('Test recursive solution.')
    stairs = 1
    assert climb_stairs_recursive(stairs) == 1

    stairs = 2
    assert climb_stairs_recursive(stairs) == 2

    stairs = 3
    assert climb_stairs_recursive(stairs) == 3

    stairs = 4
    assert climb_stairs_recursive(stairs) == 5  # [1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2]

    stairs = 10
    assert climb_stairs_recursive(stairs) == 89  # [1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2]
    print('Done testing recursive.')
    print('Tests passed.')
