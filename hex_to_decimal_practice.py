conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                    '5': 5, '6': 6, '7': 7,
                    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
                    'D': 13, 'E': 14, 'F': 15}

def hex_to_dec_rec(hex): 
    return 

def hex_to_dec_iter(hex):     
    return 

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
