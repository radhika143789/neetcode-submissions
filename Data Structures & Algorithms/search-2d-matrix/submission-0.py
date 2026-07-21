class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)     # Number of rows
        n = len(matrix[0])  # Number of columns
        
        # Initialize binary search pointers for the virtual 1D array
        left = 0
        right = (m * n) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Map the 1D mid index back to 2D row and column
            row = mid // n
            col = mid % n
            
            virtual_val = matrix[row][col]
            
            if virtual_val == target:
                return True
            elif virtual_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False