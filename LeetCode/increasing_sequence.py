def increasingTriplet(nums: list[int]) -> bool:
    first = float('inf')
    second = float('inf')
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False


nums = [50, 60, 70, 1, 0]
increasingTriplet(nums)
