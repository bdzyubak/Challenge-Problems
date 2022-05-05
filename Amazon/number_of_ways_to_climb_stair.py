def number_of_ways(steps): 
    # Can take one or two steps to reach final steps
    # Return number of ways in which this can be done
    if steps<1: 
        return 0
    elif steps == 1: 
        return 1
    num_ways_just_ones = 1
    num_ways_with_twos = sum_ways_by_twos(steps)
    
    num_ways_total = num_ways_just_ones + num_ways_with_twos
    print('There are ' + str(num_ways_total) + ' ways to do this with ' + str(steps) + ' steps.')
    return num_ways_just_ones + num_ways_with_twos

def sum_ways_by_twos(steps): 
    num_ways_by_twos = 0
    n = steps
    while n>1: 
        num_ways_by_twos += n-1
        n-=2
    return num_ways_by_twos


if __name__ == '__main__': 
    assert number_of_ways(0) == 0, 'Test did not work for 0 steps'

    assert number_of_ways(1) == 1, 'Test did not work for 1 steps'

    assert number_of_ways(2) == 2, 'Test did not work for 2 steps'

    assert number_of_ways(3) == 3, 'Test did not work for 3 steps'

    assert number_of_ways(4) == 5, 'Test did not work for 4 steps'

    assert number_of_ways(5) == 7, 'Test did not work for 5 steps'

    