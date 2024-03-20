def canJump(nums: list[int]) -> bool:
    max_distance = 0
    for i in range(0, len(nums) - 1):
        max_distance = max(max_distance, nums[i])
        if max_distance <= 0:
            return False
        max_distance -= 1
    return True
