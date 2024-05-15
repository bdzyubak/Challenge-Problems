# Implement function count_numbers that accepts a sorted list of unique integers and, efficiently with respect to time used, counts the number of list elements that are less than the parameter less_than.
#
# For example, count_numbers([1, 3, 5, 7], 4) should return 2 because there are two list elements less than 4.


def count_numbers(sorted_list, less_than):
    count_lower = 0
    for val in sorted_list:
        if val < less_than:
            count_lower += 1
        else:
            break
    return count_lower


sorted_list = [1, 3, 4, 5, 7]
assert count_numbers(sorted_list, 4) == 2
print('Tests passed.')
