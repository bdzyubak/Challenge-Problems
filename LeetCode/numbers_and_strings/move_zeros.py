def moveZeroes(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    count = 0
    while i < len(nums):
        if nums[i] == 0:
            nums.pop(i)
            count += 1
        else:
            i += 1

    nums += [0] * count
