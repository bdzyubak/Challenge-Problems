import time
from random import randint


def max_min(k, arr):
    arr.sort()
    unfairness_score = list()
    for i in range(len(arr) - k + 1):
        kernel = arr[i:(i + k)]
        unfairness_score.append(kernel[-1] - kernel[0])  # Equivalent to max/min since array is sorted
    # print(min(unfairness_score))
    return min(unfairness_score)


def min_max_original(k, arr):
    arr.sort()
    unfairness_score = list()
    for i in range(len(arr) - k + 1):
        kernel = arr[i:(i + k)]
        unfairness_score.append(max(kernel) - min(kernel))  # Equivalent to max/min since array is sorted
    # print(min(unfairness_score))
    return min(unfairness_score)


if __name__ == '__main__':
    array = [100, 200, 300, 350, 400, 401, 402]
    random_array = [randint(1, 1000000) for i in range(1000000)]
    k = 10000
    start = time.time()
    max_min(k, random_array)
    end = time.time()
    print(end - start)

    start = time.time()
    min_max_original(k, random_array)
    end = time.time()
    print(end - start)
    print('Done.')
