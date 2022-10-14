# fib_dict = dict()
fib_dict = {2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34}
fib_dict_init = {2: 1, 3: 2}

def fib(n): 
   if n <= 0: 
       return 0
   if n<=1: 
       return n   
   return fib(n-1) + fib(n-2)

def fib_record(n): 
    if n in fib_dict_init: 
        return fib_dict_init[n]
    if n <= 0: 
        return 0
    elif n <=1: 
        return n
    return fib(n-1) + fib(n-2)

def test_fib(): 
    for key in fib_dict: 
        
        result = fib(key)
        assert result == fib_dict[key]

    # for key in fib_dict: 
    #     result = fib_record(key)
    #     assert result == fib_dict[key]

if __name__ == '__main__': 
    test_fib()
    print('Done.')