class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i, j = 0, 0

        result = 0
        while j < len(prices):
            if prices[i] <= prices[j]:
                result = max(result, prices[j] - prices[i])
                j += 1
            else:
                i += 1
        
        return result
        
        