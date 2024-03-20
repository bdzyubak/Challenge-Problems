def maxArea(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_water = 0
    while left < right:
        water = min(height[left], height[right]) * (right - left)
        if height[right] > height[left]:
            left += 1
        else:
            right -= 1
        max_water = max(max_water, water)
    return max_water