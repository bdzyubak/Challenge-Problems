def dec_to_bin_rec(dec): 
   
    return 

def dec_to_bin_iter(dec): 
    
    return 

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
