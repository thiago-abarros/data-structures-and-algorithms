from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n_cols = len(board[0])
        n_rows = len(board)

        for row in range(n_rows):
            for column in range(n_cols):
                if self.backtrack(board, n_rows, n_cols, row, column, word):
                    return True
        return False
    
    def backtrack(self, board, n_rows, n_cols, row, column, suffix):
        if len(suffix) == 0:
            return True
        
        if (column == n_cols or column < 0 or 
            row == n_rows or row < 0 or 
            board[row][column] != suffix[0]):
            return False 

        board[row][column] = "#"                
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for row_offset, column_offset in directions:
            res = self.backtrack(board, n_rows, n_cols, row + row_offset, column + column_offset, suffix[1:])

            if res:
                return True 
            
        board[row][column] = suffix[0]