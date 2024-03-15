# Limit solution memory space to O(1) i.e. don't use hash map

def twoSum(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    while left <= right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left + 1, right + 1]  # Convert to 1-indexed
        elif sum < target:
            left += 1
        elif sum > target:
            right -= 1
