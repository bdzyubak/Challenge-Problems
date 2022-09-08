def climb_stairs_iterative(stairs): 
   
    return 

def climb_stairs_recursive(stairs): 
    return 

def climb_stairs_rec(stairs): 
    
    return 


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