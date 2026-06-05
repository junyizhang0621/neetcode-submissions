class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        i, j = 0, 1


        profit = 0

        while j < len(prices):
            buy, sell = prices[i], prices[j]

            if buy < sell:
                profit += sell - buy
                i += 1
            else:
                i =j
            j += 1
        
        return profit