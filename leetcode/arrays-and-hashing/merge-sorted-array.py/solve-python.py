from typing import List
"""
    Constraints:

    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length_nums1 = m - 1
        length_nums2 = n - 1
        max_length = m + n - 1
        
        while length_nums2 >= 0:
            if length_nums1 >= 0 and nums1[length_nums1] > nums2[length_nums2]:
                nums1[max_length] = nums1[length_nums1]
                length_nums1 -= 1
            else:
                nums1[max_length] = nums2[length_nums2]
                length_nums2 -= 1
            max_length -= 1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

solution = Solution().merge(nums1, 3, nums2, 3)
print("solução: " + str(solution))