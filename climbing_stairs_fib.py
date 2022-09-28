from sympy import N


def climb_stairs_recursive(stairs): 
    return climb_stairs_rec(stairs)

def climb_stairs_rec(stairs): 
    if stairs <= 2: 
        return stairs
    ways_after_taking_one_step = climb_stairs_rec(stairs-1)
    ways_after_taking_two_steps = climb_stairs_rec(stairs-2)
    return ways_after_taking_one_step + ways_after_taking_two_steps

if __name__ == '__main__': 
    # print('Test iterative solution.')
    # stairs = 1
    # assert climb_stairs_iterative(stairs) == 1

    # stairs = 2
    # assert climb_stairs_iterative(stairs) == 2

    # stairs = 3
    # assert climb_stairs_iterative(stairs) == 3

    # stairs = 4
    # assert climb_stairs_iterative(stairs) == 5 #[1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2]
    # print('Done.')

    print('Test recursive solution.')
    stairs = 1
    assert climb_stairs_recursive(stairs) == 1

    stairs = 2
    assert climb_stairs_recursive(stairs) == 2

    stairs = 3
    assert climb_stairs_recursive(stairs) == 3

    stairs = 4
    assert climb_stairs_recursive(stairs) == 5 #[1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2]
    
    stairs = 10
    assert climb_stairs_recursive(stairs) == 89 #[1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2]
    print('Tests passed.')