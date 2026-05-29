class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 0
        profit = 0
        while j < len(prices):
            buy = prices[i]
            sell = prices[j]


            cur_profit = max(sell - buy, 0)
            profit = max(cur_profit, profit)

            if buy <= sell:
                j += 1
            
            else:
                i += 1
            
        return profit
