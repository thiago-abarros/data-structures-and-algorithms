from typing import List 
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n_rows = len(board)
        n_columns = len(board[0])
        
        if len(word) > n_rows * n_columns:
            return False
        
        count = Counter(sum(board, []))
        
        for column, countWord in Counter(word).items():
            if count[column] < countWord:
                return False
            
        if count[word[0]] > count[word[-1]]:
             word = word[::-1]
                        
        seen = set()
        
        def dfs(row, column, i):
            
            if i == len(word):
                return True
            
            if row < 0 or column < 0 or row >= n_rows or column >= n_columns or word[i] != board[row][column] or (row, column) in seen:
                return False
            
            seen.add((row, column))
            res = (
                dfs(row + 1, column, i+1) or 
                dfs(row - 1, column, i+1) or
                dfs(row, column + 1, i+1) or
                dfs(row, column - 1, i+1) 
            )
            seen.remove((row, column)) # backtracking

            return res
        
        for i in range(n_rows):
            for j in range(n_columns):
                if dfs(i, j, 0):
                    return True
        return False