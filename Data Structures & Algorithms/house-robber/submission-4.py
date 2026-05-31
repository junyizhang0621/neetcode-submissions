class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
        
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]

            res1 = nums[i] + dfs(i + 2)
            res2 = dfs(i+1)
            dp[i] = max(res1, res2)
            return dp[i]        
        return dfs(0)