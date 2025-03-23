from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 != 0:
            a = len(nums1) // 2
            return nums1[a]
        else:
            a = len(nums1) // 2
            b = (nums1[a-1] + nums1[a]) / 2
            return b

sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2]))
print(sol.findMedianSortedArrays([1, 2], [3, 4]))
print(sol.findMedianSortedArrays([0, 0], [0, 0]))
print(sol.findMedianSortedArrays([], [1]))
print(sol.findMedianSortedArrays([2], []))