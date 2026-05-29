class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(a):
            if a == 0:
                return 0
            if a in dp:
                return dp[a]
            if a < 0:
                return float('inf')
            
            count = float('inf')
            for i in coins:
                result = dfs(a - i)
                if result != float('inf'):
                    count = min(count, result + 1)
            
            dp[a] = count

            return count
        
        result = dfs(amount)

        return result if result != float('inf') else -1


        