

def chaos(q): 
    # print('New Example:') 
    q = [n-1 for n in q] # Shift original positions to zero-index
    print(q)
    counter = 0
    for ind,value in enumerate(q): 
        if (value-ind)>2: 
            str = 'Too chaotic'
            # print(str)
            return(str)
        # print('Two ahead:')
        ahead = q[max(0,value-1):ind]
        # print(ahead)
        for candidate in ahead: 
            if candidate>value: 
                counter += 1
    return counter


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

