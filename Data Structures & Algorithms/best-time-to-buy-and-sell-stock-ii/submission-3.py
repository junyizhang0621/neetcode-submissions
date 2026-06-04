class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        i, j = 0, 1


        profit = 0

        while j < len(prices):
            buy, sell = prices[i], prices[j]

            if buy >= sell:
                i +=1
                j+=1
            else:
                profit += (sell- buy)
                j += 1
                i+=1
        
        return profit
            