def summaryRanges(nums: list[int]) -> list[str]:
    ranges = list()
    if not nums:
        return ranges

    range_start = nums[0]
    for ind in range(1, len(nums)):
        if (nums[ind] - nums[ind - 1] > 1):
            # Report
            print(f"Reporting on ind {ind} val {nums[ind]}")
            if nums[ind - 1] == range_start:
                ranges.append(f"{nums[ind - 1]}")
            else:
                ranges.append(f"{range_start}->{nums[ind - 1]}")
            range_start = nums[ind]

    if nums[-1] == range_start:
        ranges.append(f"{nums[-1]}")
    else:
        ranges.append(f"{range_start}->{nums[-1]}")

    return ranges


nums = [0,1,2,4,5,7]
assert summaryRanges(nums) == ["0->2","4->5","7"]

nums = [0,2,3,4,6,8,9]
assert summaryRanges(nums) == ["0","2->4","6","8->9"]
