def canJump(nums: list[int]) -> bool:
    jump = 1
    for num in nums:
        jump -= 1
        if jump < 0:
            return False
        jump = max(jump, num)

    return True
