#
# nums = [2,2,1,1,1,2,2]
# current_highest = 1
# most_freq = nums[0]
# for i in nums:
#     curr_freq = nums.count(i)
#     if curr_freq > current_highest:
#         current_highest = curr_freq
#         most_freq = i
# print(most_freq)



nums = [3,2,3]
occur = dict()
occur_thresh = len(nums) / 2
for num in nums:
    if num not in occur:
        occur[num] = 1
    else:
        print(f"{occur[num]} {occur_thresh}")
        occur[num] += 1
        if occur[num] > occur_thresh:
            print(f"Returned {num}")


# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         current_highest = 0
#         for i in range(len(nums)):
#             curr_freq = nums.count(i)
#             if curr_freq > current_highest:
#                 current_highest = curr_freq
#                 most_freq = nums[i]
#
#         return most_freq


# Slower, more roundabout
# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         elements = dict()
#         for i in range(len(nums)):
#             if nums[i] in elements:
#                 elements[nums[i]] += 1
#             else:
#                 elements[nums[i]] = 1
#
#         highest_occurance = max(elements.values())
#         val_with_highest_occurance = [val for val in elements if elements[val] == highest_occurance][0]
#         return val_with_highest_occurance