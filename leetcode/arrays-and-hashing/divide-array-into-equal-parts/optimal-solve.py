from typing import List 
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Cria um dicionário formado por um valor e 
        # a quantidade de vezes que ele aparece no array
        counter = Counter(nums)
        for count in counter.values():
            # Caso a quantidade de vezes que ele aparece 
            # for ímpar, quer dizer que não há como fazer os pares
            if count%2 == 1:
                return False
        
        return True 

list_solve = [9,4,18,3,2,6,18,15,7,15,6,4,15,14,7,4,15,4,3,17,9,13,13,12,2,14,12,17]
list_solve2 = [1,2,3,4,5,6]
solution = Solution().divideArray(list_solve)
print(solution)