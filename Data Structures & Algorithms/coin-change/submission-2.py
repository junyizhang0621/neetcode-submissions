class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        res = 1e9
        dp = {}

        def dfs(amount):
            if amount == 0:
                return 0
            
            if amount in dp:
                return dp[amount]

            
            res = 1e9
            for i in coins:
                if amount - i >= 0:
                    res = min(res, 1+ dfs(amount - i))
            dp[amount] =  res
            return res
        
        minCoins = dfs(amount)
        if minCoins >= 1e9:
            return -1
        else:
            return minCoins
        return dfs(amount)
            
