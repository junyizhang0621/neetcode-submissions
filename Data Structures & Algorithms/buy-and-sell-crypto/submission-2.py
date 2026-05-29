class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        i, j = 0, 0

        while j < len(prices):
            if prices[i] <= prices[j]:
                profit = max(profit, prices[j] - prices[i])
                j += 1
            else:
                i+=1
            
        return profit
            
        