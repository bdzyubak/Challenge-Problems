conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}

def dec_to_hex_rec(dec): 
    remaining_digits = dec // 16 
    last_digit = dec % 16
    if remaining_digits == 0: 
        return conversion_table[last_digit]
    return dec_to_hex_rec(dec // 16) + conversion_table[last_digit]

def dec_to_hex_iter(dec): 
    if dec == 0: 
        return '0'
    hex = ''
    while dec > 0: 
        hex = conversion_table[dec % 16] + hex
        dec = dec // 16
    
    return hex

def use_builtin_to_test(num): 
    bin_string = hex(num)[2:].upper()
    return bin_string

def test_digits(fun): 
    for i in range(21): 
        binary_i = use_builtin_to_test(i)
        print(str(i) + ' = ' + str(binary_i))
        assert fun(i) == use_builtin_to_test(i), 'Decimal ' + str(i) + ' comes out to: ' + fun(i) + '. Should be: ' + str(binary_i)

if __name__ == '__main__': 
    # print('Testing Recursive.')
    # test_digits(dec_to_hex)
    # print('Done testing Recursive.')

    print('Testing iterative.')
    test_digits(dec_to_hex_iter)
    print('Done testing iterative.')

    print('Testing recursive.')
    test_digits(dec_to_hex_rec)
    print('Done testing recursive.')
