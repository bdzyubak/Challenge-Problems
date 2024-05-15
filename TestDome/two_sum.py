# Write a function that, when passed a list and a target sum, returns, efficiently with respect to time used, two distinct zero-based indices of any two of the numbers, whose sum is equal to the target sum.
#
# If there are no two numbers, the function should return None.
#
# For example, find_two_sum([3, 1, 5, 7, 5, 9], 10) should return a single tuple containing any of the following pairs of indices:

def find_two_sum(numbers, target_sum):
    # :param numbers: (list of ints) The list of numbers.
    # :param target_sum: (int) The required target sum.
    # :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    occur = dict()
    for i, num in enumerate(numbers):
        diff = target_sum - num
        if diff in occur:
            return (i, occur[diff])
        occur[diff] = i
    return None


result = find_two_sum([3, 1, 5, 7, 5, 9], 10)
assert result == (0, 3) or result == (2, 4) or result == (3, 0) or result == (4, 2)
print('Tests passed.')
