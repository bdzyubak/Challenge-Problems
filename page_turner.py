
def min_turns(n,p): 
    turns_from_left = p//2
    turns_from_right = (n-p)//2
    return (min(turns_from_left,turns_from_right))

if __name__ == '__main__': 
    assert min_turns(3,1) == 0

    assert min_turns(3,3) == 0

    assert min_turns(3,2) == 0
    
    assert min_turns(4,1) == 0

    assert min_turns(4,4) == 0

    assert min_turns(4,3) == 0

    assert min_turns(4,2) == 1

    assert min_turns(1,1) == 0

    assert min_turns(2,2) == 0

    assert min_turns(10,6) == 2

    assert min_turns(10,5) == 2

    assert min_turns(11,6) == 2

    assert min_turns(11,5) == 2
    print('All Passed.')
    