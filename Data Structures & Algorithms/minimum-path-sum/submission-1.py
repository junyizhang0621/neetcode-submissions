class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        res = [[-1] * (cols) for _ in range(rows)]
        def dfs(r, c):
            if r == rows - 1 and c ==cols - 1:
                return grid[r][c]
            
            if r == rows or c == cols:
                return float('inf')
            
            if res[r][c] != -1:
                return res[r][c]

            res[r][c] = grid[r][c] + min(dfs(r + 1, c), dfs(r, c+1))
            return res[r][c]
        return dfs(0, 0)

        
        