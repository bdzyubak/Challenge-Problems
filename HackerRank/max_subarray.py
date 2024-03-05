def maxSubarray(arr):
    print('New Example: ')
    # print(arr)
    if max(arr) <= 0:
        return max(arr), max(arr)

    sequence_sum = 0
    max_left_bound = max_ending_here = 0
    for i in arr:
        max_left_bound = max(i, max_left_bound + i)
        max_both_bounds = max(max_both_bounds, max_left_bound)
        if i > 0:
            sequence_sum += i

    return max_both_bounds, sequence_sum


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    assert maxSubarray(arr) == (10, 10)

    arr = [2, -1, 2, 3, 4, -5]
    assert maxSubarray(arr) == (10, 11)
    print('Done.')
