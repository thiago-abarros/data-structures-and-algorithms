from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        count_num = 0
        num = 9999
        for i in range(len(nums)):
            if nums[i] == num:
                count_num += 1
                if count_num < 2:
                    nums[index] = nums[i]
                    index += 1
            else:
                    nums[index] = nums[i]
                    num = nums[i]
                    index += 1
                    count_num = 0
        nums = nums[:index]
        print("lista: " + str(nums))

list_nums = [0,0,1,1,1,1,2,3,3]
solution = Solution().removeDuplicates(list_nums)