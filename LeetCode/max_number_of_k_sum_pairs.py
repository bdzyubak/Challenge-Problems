def maxOperations(nums: list[int], k: int) -> int:
    nums_dict = dict()
    num_actions = 0

    for num in nums:
        if (k - num) in nums_dict:
            if nums_dict[k - num] == 1:
                del nums_dict[k - num]
            else:
                nums_dict[k - num] -= 1
            num_actions += 1

        else:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

    return num_actions
