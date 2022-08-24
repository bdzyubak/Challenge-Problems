def bin_to_dec(bin_string): 
    return bin_to_dec_recursive(bin_string)

def bin_to_dec_iterative(bin_string): 
    dec = 0
    while bin_string: 
        dec += int(bin_string[0]) * 2**(len(bin_string)-1)
        bin_string = bin_string[1:]
    return dec

def bin_to_dec_recursive(bin_string): 
    if not bin_string: 
        return 0
    dec = int(bin_string[0]) * 2**(len(bin_string)-1) + bin_to_dec(bin_string[1:])
    return dec

if __name__ == "__main__": 
    n = '0'
    assert bin_to_dec(n) == 0 

    n = '1'
    assert bin_to_dec(n) == 1

    n = '10'
    assert bin_to_dec(n) == 2

    n = '11'
    assert bin_to_dec(n) == 3

    n = '100'
    assert bin_to_dec(n) == 4

    n = '101'
    assert bin_to_dec(n) == 5

    n = '110'
    assert bin_to_dec(n) == 6

    n = '111'
    assert bin_to_dec(n) == 7

    n = '1000'
    assert bin_to_dec(n) == 8

    n = '1001'
    assert bin_to_dec(n) == 9

    n = '1010'
    assert bin_to_dec(n) == 10

    n = '1011'
    assert bin_to_dec(n) == 11

    n = '1100'
    assert bin_to_dec(n) == 12 
    print('Done.')