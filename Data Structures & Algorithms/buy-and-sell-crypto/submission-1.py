class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <=1:
            return 0

        profit = 0
        i, j = 0, 1

        while j < len(prices):
            cur_profit = prices[j] - prices[i]
            profit = max(profit, cur_profit)

            if prices[i] <= prices[j]:
                j+= 1
            else:
                i += 1
        return profit


        