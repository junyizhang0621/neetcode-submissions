class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)

        def dfs(n):

            if n <= 2:
                memo[n] = n
                return n
            
            if memo[n]:
                return memo[n]
            memo[n] = dfs(n-1) + dfs(n-2)
            return memo[n]
        
        return dfs(n)
