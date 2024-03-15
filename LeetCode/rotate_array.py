from copy import deepcopy

# The real solution that is used in all practical applications without wrapping in a function. So, it's "in-place"
# Must have nums[:] for pass by reference/wrapper requirement. nums = doesn't update in place.
def rotate(nums: list[int], k: int) -> None:
    steps = k % len(nums)
    nums[:] = nums[-steps:] + nums[:-steps]
    return nums
