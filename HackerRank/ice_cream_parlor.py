def icecreamParlor(m, arr):
    for i_first, first in enumerate(arr): 
        for i_second, second in enumerate(arr[i_first+1:]): 
            if first + second == m: 
                return sorted([i_first+1,i_second+i_first+2])            

if __name__ == '__main__': 
    m = 4 
    arr = [1, 4, 5, 3, 2]
    assert icecreamParlor(m,arr) == [1,4]

    m = 4 
    arr = [2, 2, 4, 3]
    assert icecreamParlor(m,arr) == [1,2]
    print('Done.')