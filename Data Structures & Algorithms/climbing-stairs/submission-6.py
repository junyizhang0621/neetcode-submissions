class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = {}
        def dfs(i):
            if i <= 2:
                return i
            
            if i in dp:
                return dp[i]
            
            res = dfs(i-1) + dfs(i-2)

            dp[i] = res
            return dp[i]
        return dfs(n)