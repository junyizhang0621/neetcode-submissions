class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        hash_table = {}

        def dfs(i, holding):
            if i == len(prices):
                return 0

            if (i, holding) in hash_table:
                return hash_table[(i, holding)]

            if not holding:
                skip = dfs(i + 1, False)
                buy = -prices[i] +  dfs(i + 1, True)
                
                hash_table[(i, holding)] = max(skip, buy)
            
            else:

                hold = dfs(i+1, True)
                sell = prices[i] + dfs(i+1, False)

                hash_table[(i, holding)] = max(hold, sell)
            
            return hash_table[(i, holding)] 
        
        return dfs(0, False)

