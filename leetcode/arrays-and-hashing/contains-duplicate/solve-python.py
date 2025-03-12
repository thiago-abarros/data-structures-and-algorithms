from typing import List

"""
Examples: 

Ex 1: 
    input: nums = [1,2,3,1]
    output: True
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set()

        for num in nums: 
            if num in hash:
                return True 
            hash.add(num)
        return False 

list_example = [1,2,3,2]
solutionClass = Solution()
print(solutionClass.containsDuplicate(list_example))
