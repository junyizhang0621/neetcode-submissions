class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            mid = (top + bot)//2

            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                break
        
        if top > bot:
            return False
        
        l, r = 0, len(matrix[0])
        row = (top + bot)//2

        while l <= r:
            mid = (r + l) // 2
            if matrix[row][mid] == target:
                return True
            
            if matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False


