def bin_to_dec_iter(bin): 
    
    return 

def bin_to_dec_rec(bin): 
    
    return 

def use_builtin_to_test(num): 
    bin_string = bin(num)[2:]
    return bin_string

def test_digits(fun): 
    for i in range(11): 
        binary_i = use_builtin_to_test(i)
        print(str(i) + ' = ' + str(binary_i))
        assert fun(binary_i) == i, 'Binary ' + binary_i + ' comes out to: ' + fun(binary_i) + '. Should be: ' + str(i)

if __name__ == '__main__': 
    print('Testing Recursive.')
    test_digits(bin_to_dec_rec)
    print('Done testing Recursive.')
    
    print('Testing Iterative.')
    test_digits(bin_to_dec_iter)
    print('Done testing Iterative.')


