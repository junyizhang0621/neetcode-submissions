class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c = float('inf')
        last_idx = len(cost)

        dp = [0] *(last_idx)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, last_idx):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        return min(dp[-1], dp[-2])