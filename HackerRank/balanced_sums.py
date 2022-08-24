def balancedSums(arr):
    print('The new array is: ')
    print(arr)
    value_exists = 'NO'
    
    i = len(arr)//2
    left_sum = sum_left(arr,i)
    right_sum = sum_right(arr,i)
    if left_sum > right_sum: 
        direction = 'left'
    elif right_sum > left_sum: 
        direction = 'right'
    else: 
        return 'YES'
    value_exists = check_sum_shift(arr,i,value_exists,direction)
    return value_exists

def check_sum_shift(arr,i,value_exists,direction): 
    # print(arr[:(i)])
    # print(arr[(i+1):])
    if value_exists == 'NO' and i>=0 and i<=len(arr): 
        if direction == 'left': 
            i-=1
        else: 
            i+=1
        left_sum = sum_left(arr,i)
        right_sum = sum_right(arr,i)
        print('i is: ' + str(i))
        print('Left sum is: ' + str(left_sum))
        print('Right sum is: ' + str(right_sum))
        if left_sum == right_sum: 
            value_exists = 'YES'
        value_exists = check_sum_shift(arr,i,value_exists,direction)
    return value_exists

def sum_left(arr,i): 
    return sum(arr[:i])

def sum_right(arr,i): 
    return sum(arr[(i+1):])

if __name__ == '__main__': 
    arr = [1,2,3]
    assert balancedSums(arr) == 'NO'

    arr = [1,2,3,3] 
    assert balancedSums(arr) == 'YES'

    arr = [1,1,4,1,1]
    assert balancedSums(arr) == 'YES'

    arr = [2,0,0,0]
    assert balancedSums(arr) == 'YES'

    arr = [0,0,2,0]
    assert balancedSums(arr) == 'YES'
    print('Done')