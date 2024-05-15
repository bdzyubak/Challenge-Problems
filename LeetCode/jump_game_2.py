nums = [2, 3, 1, 1, 4]
i = 0
j = 0
count_jumps = 1
while i < len(nums) - 1:
    max_jump = 0
    j = i + 1
    while j < (i + nums[i]) and j < len(nums):
        # print(f"{i} {j} {max_jump}")
        max_jump = max(max_jump, nums[i] + i)
        j += 1
    i += max_jump
    # print(f"{i}")
    count_jumps += 1

print(count_jumps)


def jump(self, nums: List[int]) -> int:
    min_pos = 0
    max_pos = 0
    jumps = 0
    while max_pos < len(nums) - 1:
        best_jump = 0
        for i in range(min_pos, max_pos + 1):
            best_jump = max(best_jump, i + nums[i])
        min_pos = max_pos + 1
        max_pos = best_jump
        jumps += 1
    return jumps