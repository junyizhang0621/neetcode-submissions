class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1:
            return 0
        
        profit = 0

        i, j = 0, 1

        while j < len(prices):
            buy, sell = prices[i], prices[j]

            if sell <= buy:
                i=j
                j+=1
        
            else:
                profit = max(profit, sell - buy)
                j+=1
        
            
            
        return profit
            