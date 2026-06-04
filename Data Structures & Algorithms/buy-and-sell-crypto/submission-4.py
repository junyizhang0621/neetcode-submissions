class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        i, j = 0, 0

        while j < len(prices):
            buy, sell = prices[i], prices[j]

            if sell <= buy:
                i=j
            else:
                profit = max(profit, sell - buy)
            
            j+=1
        
        return profit
            