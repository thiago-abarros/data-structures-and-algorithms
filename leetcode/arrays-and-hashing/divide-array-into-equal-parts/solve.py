from typing import List 

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        if nums[::2] != nums[1::2]:
            return False
        
        return True

list_solve = [9,4,18,3,2,6,18,15,7,15,6,4,15,14,7,4,15,4,3,17,9,13,13,12,2,14,12,17]
list_solve2 = [1,2,3,4,5,6]
solution = Solution().divideArray(list_solve)
print(solution)