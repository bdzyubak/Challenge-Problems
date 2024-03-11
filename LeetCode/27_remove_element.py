class Solution:
    class Solution:
        def removeElement(self, nums: list[int], val: int) -> int:
            # Test on Leetcode is buggy. If count droppedi s returned, it says the answer is wrong. If wrong num
            # elements not matching val is returned - it's ok
            num_len = len(nums)
            i = num_len - 1
            # count_dropped = 0
            while i >= 0:
                if nums[i] == val:
                    nums.pop(i)
                    # count_dropped += 1
                i -= 1
            return len(nums)  # - count_dropped