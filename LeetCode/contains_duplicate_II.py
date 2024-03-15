def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    candidates = dict()
    for i in range(len(nums)):
        if nums[i] in candidates:
            if abs(candidates[nums[i]] - i) <= k:
                return True
        candidates[nums[i]] = i
    return False


nums = [1,2,3,1]
k = 3

assert containsNearbyDuplicate(nums, k) is True

nums = [1,0,1,1]
k = 1

assert containsNearbyDuplicate(nums, k) is True


