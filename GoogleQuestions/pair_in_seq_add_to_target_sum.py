
# The task in this interview question is: given a sequence of numbers (A), find a pair of numbers that add up to a second input argument (B). There may not be a valid pair. 

def find_pair_in_seq_naive(seq_of_nums,target_sum): 
    # This is the most basic solution which does a greedy search. 
    # An option exists to copy the list for second iteration and pop index of first number during each iteration. 
    # However, this is not a major efficiency improvement
    sum_equals_target = False
    pair_of_nums = ''
    for index_first_number, value_first_number in enumerate(seq_of_nums): 
        for index_second_number, value_second_number in enumerate(seq_of_nums): 
            if index_second_number != index_first_number: 
                sum_equals_target = target_sum == (value_first_number + value_second_number)
                if sum_equals_target: 
                    pair_of_nums = [value_first_number, value_second_number]
                    break
    
    print_output(pair_of_nums)
    return pair_of_nums


def find_pair_in_seq_complement(seq_of_nums,target_sum): 
    # Given a number, check if any remaining number complements it to make sum. 
    # Check/assume - numbers can be negative - cannot exclude numbers higher than sum. 
    pair_of_nums = ''
    for num in seq_of_nums: 
        complement = target_sum - num
        if complement in seq_of_nums: 
            pair_of_nums = [num,complement]
            break

    print_output(pair_of_nums)
    return pair_of_nums


def find_pair_in_seq_complement_sorted(seq_of_nums,target_sum): 
    # Additionally assume numbers are sorted to make search more efficient 
    # No need to return to numbers once they've been searched. 
    # Any sequence could be sorted as a first step in this approach
    while seq_of_nums: 
        num = seq_of_nums.pop()
        complement = target_sum - num
        if complement in seq_of_nums: 
            pair_of_nums = [num,complement]
    
    print_output(pair_of_nums)
    return pair_of_nums


def find_pair_in_seq_iterative(seq_of_nums,target_sum): 
    # Linearly search the space by bounding numbers and relying on sorted order. 
    # Take lowest number and advance highest until it's about to be too high. 
    # Advance lowest number until valid pair is found, or return no match. 
    ind_smaller = 0
    ind_larger = 1 
    pair_of_nums = ''
    while not pair_of_nums and ind_larger<=len(seq_of_nums): 
        sum_of_ints = seq_of_nums[ind_smaller] + seq_of_nums[ind_larger]
        if sum_of_ints == target_sum: 
            # The smallest possible sum is (now) too high - no valid pair
            # No need to set sum_equals_target to True, as return will exit loop
            pair_of_nums = [seq_of_nums[ind_smaller],seq_of_nums[ind_larger]]
        elif sum_of_ints < target_sum: 
            ind_larger += 1
    
    while not pair_of_nums and ind_smaller < ind_larger: 
        sum_of_ints = seq_of_nums[ind_smaller] + seq_of_nums[ind_larger]
        if sum_of_ints == target_sum: 
            # The smallest possible sum is (now) too high - no valid pair
           pair_of_nums = [seq_of_nums[ind_smaller],seq_of_nums[ind_larger]]
        elif sum_of_ints < target_sum: 
            ind_smaller += 1
    
    print_output(pair_of_nums)
    return pair_of_nums


def print_output(numbers): 
    if numbers: 
        print('Found valid pair: ' + str(numbers[0]) + ', ' + str(numbers[1]))
    else: 
        print('No valid pair found.')
