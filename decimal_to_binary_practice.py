def dec_to_bin_rec(dec): 
    if dec == 0: 
        return '0'
    if dec == 1: 
        return '1'
    return dec_to_bin_rec(dec // 2) + str(dec % 2)

def dec_to_bin_iter(dec): 
    if dec == 0: 
        return '0'
    if dec == 1: 
        return '1'
    
    bin = ''
    while dec>1: 
        bin = str(dec % 2) + bin
        dec = dec // 2
    bin = '1' + bin
    return bin

def use_builtin_to_test(num): 
    bin_string = bin(num)[2:]
    return bin_string

def test_digits(fun): 
    for i in range(11): 
        binary_i = use_builtin_to_test(i)
        print(str(i) + ' = ' + str(binary_i))
        assert fun(i) == use_builtin_to_test(i), 'Decimal ' + str(i) + ' comes out to: ' + fun(i) + '. Should be: ' + str(binary_i)

if __name__ == '__main__': 
    print('Testing Recursive.')
    test_digits(dec_to_bin_rec)
    print('Done testing Recursive.')

    print('Testing iterative.')
    test_digits(dec_to_bin_iter)
    print('Done testing iterative.')
