def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)-1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

if __name__ == '__main__': 
    # assert findZigZagSequence([1,2,3,4,5,6,7],7) == [1, 2, 3, 7, 6, 5, 4], 'Failed to transform to zig zag sequence'

    # assert findZigZagSequence(9,[10,20,20,10,10,30,50,10,20]) == 3, 'Failed to find two socks in 10ns and 20s'
    print('Done.')


    [1,2,3,4,5]
    [1,2,3,2,5]