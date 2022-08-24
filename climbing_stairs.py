def climb_stairs_recursive(stairs): 
    return number_of_ways(stairs,0)

def number_of_ways(stairs,n_ways): 
    if stairs <= 0: 
        return 0
    if stairs == 1: 
        return 1
    if stairs == 2: 
        return 2
    n_ways += stairs - 1
    n_ways = n_ways + number_of_ways(stairs-2,n_ways)
    print('Number of stairs: ' + str(stairs) + '. Number of ways: ' + str(n_ways))
    return n_ways

def climb_stairs_iterative(stairs): 
    if stairs <=0: 
        return 0
    if stairs == 1: 
        return 1
    
    by_single_steps = 1
    by_double_or_mix = double_or_mix(stairs)
    n_ways = by_single_steps + by_double_or_mix
    return n_ways

def double_or_mix(stairs): 
    counter = 0
    while stairs >=2: 
        counter += stairs - 1
        stairs -= 2
    return counter

def climb_stairs_dynamic(stairs): 
    if stairs <=0: 
        return [0]
    ways = []
    ways.append(1) # One way for 1 stair
    ways.append(2) # Two ways for 2 stairs

    for i in range (2,stairs): 
        ways.append(climb_stairs_dynamic(i-1) + climb_stairs_dynamic(i-2))
    return ways[-1]

if __name__ == '__main__': 
    print('Test iterative solution.')
    stairs = 1
    assert climb_stairs_iterative(stairs) == 1

    stairs = 2
    assert climb_stairs_iterative(stairs) == 2

    stairs = 3
    assert climb_stairs_iterative(stairs) == 3

    stairs = 4
    assert climb_stairs_iterative(stairs) == 5 #[1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2]
    print('Done.')

    print('Test recursive solution.')
    stairs = 1
    assert climb_stairs_recursive(stairs) == 1

    stairs = 2
    assert climb_stairs_recursive(stairs) == 2

    stairs = 3
    assert climb_stairs_recursive(stairs) == 3

    stairs = 4
    assert climb_stairs_recursive(stairs) == 5 #[1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2]
    print('Done.')