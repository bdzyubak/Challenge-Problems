def climb_stairs_iterative(stairs): 
    if stairs <=0: 
        return 0 
    if stairs == 1: 
        return stairs
    n_ways = 1 # Single steps all the way
    while stairs >=2: 
        n_ways += stairs-1
        stairs -= 2
    return n_ways

def climb_stairs_recursive(stairs): 
    return climb_stairs_rec(stairs) + 1 # Adjust for first step

def climb_stairs_rec(stairs): 
    if stairs <=0: 
        return 0 
    if stairs == 1: 
        return 1
    n_ways = climb_stairs_rec(stairs-1) + climb_stairs_rec(stairs-2)
    return n_ways


if __name__ == '__main__': 
    print('Test iterative solution.')
    stairs = 1
    assert climb_stairs_recursive(stairs) == 1

    stairs = 2
    assert climb_stairs_recursive(stairs) == 2

    stairs = 3
    assert climb_stairs_recursive(stairs) == 3

    stairs = 4
    assert climb_stairs_recursive(stairs) == 5 #[1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2]
    print('Done.')

    stairs = 5
    assert climb_stairs_recursive(stairs) == 8 #[1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2]
    print('Done.')

    # print('Test recursive solution.')
    # stairs = 1
    # assert climb_stairs_recursive(stairs) == 1

    # stairs = 2
    # assert climb_stairs_recursive(stairs) == 2

    # stairs = 3
    # assert climb_stairs_recursive(stairs) == 3

    # stairs = 4
    # assert climb_stairs_recursive(stairs) == 5 #[1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2]
    # print('Done.')