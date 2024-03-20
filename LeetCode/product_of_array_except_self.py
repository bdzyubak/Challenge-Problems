def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    left = [1] * n
    right = [1] * n
    array = [1] * n

    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    for i in range(n):
        array[i] = left[i] * right[i]

    return array


nums = [1,2,3,4]
assert productExceptSelf(nums) == [24,12,8,6]

nums = [-1,1,0,-3,3]
assert productExceptSelf(nums) == [0,0,9,0,0]
