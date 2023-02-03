class Solution:
    #solution 1: More optimized using O(m + n) space:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # input validation
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])

        zeroes_row = [False] * m
        zeroes_col = [False] * n
        for row in range(m):
         for col in range(n):
             if matrix[row][col] == 0:
                 zeroes_row[row] = True
                 zeroes_col[col] = True
        for row in range(m):
         for col in range(n):
             if zeroes_row[row] or zeroes_col[col]:
                 matrix[row][col] = 0
                
		
                
    #solution 2: Most optimized using O(1) space:
    def setZeroes_2(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False
        
        # iterate through matrix to mark the zero row and cols
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0
    
        # iterate through matrix to update the cell to be zero if it's in a zero row or col
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]
                
        # update the first row and col if they're zero
        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0
        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0
