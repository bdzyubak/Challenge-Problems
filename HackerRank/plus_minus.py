def plusMinus(arr):
    count_pos = 0
    count_neg = 0
    count_zero = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count_pos += 1
        elif arr[i] < 0:
            count_neg += 1
        else:
            count_zero += 1
    ratio_pos = round(count_pos / len(arr), 6)
    ratio_neg = round(count_neg / len(arr), 6)
    ratio_zero = round(count_zero / len(arr), 6)

    print(ratio_pos)
    print(ratio_neg)
    print(ratio_zero)
