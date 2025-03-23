#O((m+n) log(m+n))
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

#O(log(m+n))
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        left, right = 0, len(nums1)
        m, n = len(nums1), len(nums2)

        while left <= right:
            x = (left + right) // 2
            y = (m + n + 1) // 2 - x

            maxLeftX = float('-inf') if x == 0 else nums1[x - 1]
            minRightX = float('inf') if x == m else nums1[x]
            maxLeftY = float('-inf') if y == 0 else nums2[y - 1]
            minRightY = float('inf') if y == n else nums2[y]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                right = x - 1
            else:
                left = x + 1

sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2]))
print(sol.findMedianSortedArrays([1, 2], [3, 4]))
print(sol.findMedianSortedArrays([0, 0], [0, 0]))
print(sol.findMedianSortedArrays([], [1]))
print(sol.findMedianSortedArrays([2], []))
