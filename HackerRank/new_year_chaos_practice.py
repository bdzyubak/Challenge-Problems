

def chaos(q): 
    
    return 


if __name__ == '__main__': 
    q = [1,2,3,5,4,6,7,8]
    assert chaos(q) == 1

    q = [4,1,2,3]
    assert chaos(q) == 'Too chaotic'
    
    q = [5, 1, 2, 3, 7, 8, 6, 4]
    assert chaos(q) == 'Too chaotic'

    q = [1, 2, 5, 3, 7, 8, 6, 4]
    assert chaos(q) == 7
    print('Done.')

