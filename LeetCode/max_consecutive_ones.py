def longestOnes(nums: list[int], k: int) -> int:
    left = 0
    count_zeros = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count_zeros += 1

        if count_zeros > k:
            if nums[left] == 0:
                count_zeros -= 1
            left += 1

    return i - left + 1


nums = [1,1,1,0,0,0,1,1,1,1,0]
assert longestOnes(nums) == 6
