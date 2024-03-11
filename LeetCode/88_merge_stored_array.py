# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To
# accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for ind_i, i in enumerate(nums1):
            for j in nums2:
                if j < i:
                    nums1[ind_i+1:] = nums1[ind_i:-1]
                    nums1[ind_i] = j
                    nums2.pop(0)
                elif i == 0:
                    nums1[ind_i] = j
                    nums2.pop(0)
                else:
                    break


def test_case_1(merge_obj):
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution = Solution
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,2,3,5,6]


def test_case_1(merge_obj):
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    Solution.merge(nums1, m, nums2, n)
    assert nums1 == [1]


def test_case_1(merge_obj):
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    Solution.merge(nums1, 1, nums2, 1)
    assert nums1 == 1
