def twoSum(nums: list[int], target: int) -> list[int]:
    candidates = dict()
    for ind, num in enumerate(nums):
        diff = target - num
        if diff in candidates:
            return [ind, candidates[diff]]
        else:
            candidates[num] = ind


nums = [2, 7, 11, 15]

target = 9
assert twoSum(nums, target) == [0, 1]
