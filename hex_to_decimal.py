conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                    '5': 5, '6': 6, '7': 7,
                    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
                    'D': 13, 'E': 14, 'F': 15}

def hex_to_dec_rec(hex): 
    if not hex: 
        return 0 
    return hex_to_dec_rec(hex[:-1])*16 + conversion_table[hex[-1]]

def hex_to_dec_iter(hex):     
    dec = 0
    power_counter = len(hex) - 1
    
    for digit in hex: 
        dec += conversion_table[digit] * 16 ** power_counter
        power_counter -= 1
    return dec

def use_builtin_to_test(num): 
    hex_string = hex(num)[2:].upper()
    return hex_string

def test_digits(fun): 
    for i in range(21): 
        hex = use_builtin_to_test(i)
        print(str(i) + ' = ' + str(hex))
        assert fun(hex) == int(hex,16), 'Hex ' + str(hex) + ' comes out to: ' + str(fun(hex)) + '. Should be: ' + str(int(hex,16))

if __name__ == '__main__': 
    print('Testing iterative.')
    test_digits(hex_to_dec_iter)
    print('Done testing iterative.')

    print('Testing recursive.')
    test_digits(hex_to_dec_rec)
    print('Done testing recursive.')
